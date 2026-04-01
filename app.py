import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="SIEM Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Load processed SIEM alerts CSV
df = pd.read_csv(
    "/Users/akshatchaturvedi/Desktop/TN GOV/processed_siem_logs.csv",
    encoding="latin1"
)

# Convert Timestamp column
df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
df["Hour"] = df["Timestamp"].dt.strftime("%H:%M")

# Add extra columns if they do not exist
if "Protocol" not in df.columns:
    protocol_list = ["HTTP", "HTTPS", "DNS", "SSH", "FTP", "SMTP"]
    df["Protocol"] = [protocol_list[i % len(protocol_list)] for i in range(len(df))]

if "Country" not in df.columns:
    country_list = ["USA", "Germany", "India", "Canada", "Private Network", "Unknown"]
    df["Country"] = [country_list[i % len(country_list)] for i in range(len(df))]

if "Username" not in df.columns:
    username_list = ["admin", "root", "veda", "guest", "user1", "analyst"]
    df["Username"] = [username_list[i % len(username_list)] for i in range(len(df))]

# Sidebar filters
st.sidebar.title("Dashboard Filters")

selected_severity = st.sidebar.selectbox(
    "Select Severity",
    ["All"] + sorted(df["severity"].dropna().unique().tolist())
)

selected_protocol = st.sidebar.selectbox(
    "Select Protocol",
    ["All"] + sorted(df["Protocol"].dropna().unique().tolist())
)

# Apply filters
filtered_df = df.copy()

if selected_severity != "All":
    filtered_df = filtered_df[
        filtered_df["severity"] == selected_severity
    ]

if selected_protocol != "All":
    filtered_df = filtered_df[
        filtered_df["Protocol"] == selected_protocol
    ]

# Page Styling
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1, h2, h3, h4, label, div, p {
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #151A24;
}

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}

div[data-testid="stDataFrame"] {
    background-color: #1E1E1E;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🛡️ SIEM Detection Dashboard")
st.subheader("SOC Monitoring Overview")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Alerts", len(filtered_df))

with col2:
    st.metric(
        "High Severity Alerts",
        len(filtered_df[filtered_df["severity"] == "HIGH"])
    )

with col3:
    st.metric(
        "Unique Source IPs",
        filtered_df["ip"].nunique()
    )

with col4:
    st.metric(
        "Alert Types",
        filtered_df["type"].nunique()
    )

# Recent Alerts Table
st.subheader("Recent Security Alerts")

display_columns = [
    "Timestamp",
    "ip",
    "type",
    "severity",
    "details",
    "Hour"
]

st.dataframe(
    filtered_df[display_columns].tail(10),
    use_container_width=True
)

# Alert Severity Distribution + Traffic by Hour
col5, col6 = st.columns(2)

with col5:
    st.subheader("Alert Severity Distribution")

    severity_data = filtered_df["severity"].value_counts().reset_index()
    severity_data.columns = ["Severity", "Count"]

    st.bar_chart(severity_data.set_index("Severity"))

with col6:
    st.subheader("Traffic by Hour")

    traffic_data = filtered_df.groupby("Hour").size().reset_index(name="Count")

    st.line_chart(traffic_data.set_index("Hour"))

# Top Suspicious IPs + Most Targeted Usernames
col7, col8 = st.columns(2)

with col7:
    st.subheader("Top Suspicious IPs")

    ip_data = filtered_df["ip"].value_counts().reset_index()
    ip_data.columns = ["IP Address", "Alert Count"]

    st.bar_chart(ip_data.head(10).set_index("IP Address"))

with col8:
    st.subheader("Most Targeted Usernames")

    username_data = filtered_df["Username"].value_counts().reset_index()
    username_data.columns = ["Username", "Count"]

    st.bar_chart(username_data.head(10).set_index("Username"))

# Protocol Usage Distribution + Suspicious Activity by Country
col9, col10 = st.columns(2)

with col9:
    st.subheader("Protocol Usage Distribution")

    protocol_data = filtered_df["Protocol"].value_counts().head(6)

    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    wedges, texts, autotexts = ax.pie(
        protocol_data.values,
        labels=protocol_data.index,
        autopct="%1.1f%%"
    )

    for text in texts:
        text.set_color("white")

    for autotext in autotexts:
        autotext.set_color("white")

    ax.axis("equal")
    st.pyplot(fig)

with col10:
    st.subheader("Suspicious Activity by Country")

    country_data = filtered_df["Country"].value_counts().reset_index()
    country_data.columns = ["Country", "Count"]

    st.bar_chart(country_data.set_index("Country"))

# Top Alert Types + Alerts by Protocol
col11, col12 = st.columns(2)

with col11:
    st.subheader("Top Alert Types")

    event_data = filtered_df["type"].value_counts().reset_index()
    event_data.columns = ["Alert Type", "Count"]

    st.bar_chart(event_data.head(10).set_index("Alert Type"))

with col12:
    st.subheader("Alerts by Protocol")

    protocol_chart_data = filtered_df["Protocol"].value_counts().reset_index()
    protocol_chart_data.columns = ["Protocol", "Count"]

    st.bar_chart(protocol_chart_data.head(10).set_index("Protocol"))

# Raw Logs Table
st.subheader("Raw Security Logs")

st.dataframe(filtered_df, use_container_width=True)
st.caption("Built by Veda | SIEM Detection Dashboard Project")
