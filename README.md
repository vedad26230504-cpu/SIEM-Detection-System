# SIEM-Detection-System

# Project Overview
This project is a SIEM-like security monitoring system built in Python to simulate a real SOC workflow. It processes authentication logs, applies multiple rule-based detection techniques to identify suspicious activity such as brute force attacks, unusual login times, high activity IPs, and potential account compromise, and enriches alerts with GeoIP information. The system also integrates Wireshark network traffic analysis to detect suspicious protocols, abnormal packet sizes, and unusual traffic patterns. High severity alerts are automatically escalated through email notifications, and the project now includes an interactive Streamlit dashboard for real-time alert monitoring, filtering, and visualization.

# Features
1. Authentication log generation and parsing
2. Brute force attack detection
3. Unusual login time detection
4. Successful login after repeated failures detection
5. High activity IP detection
6. GeoIP enrichment using IP geolocation APIs
7. Automated email alerts for high severity incidents
8. Wireshark network traffic analysis
9. Suspicious protocol detection
10. Large packet detection
11. Visualization using matplotlib charts
12. Interactive Streamlit dashboard
13. Dashboard filters for severity and protocol
14. Real-time metrics for alerts, IPs, and alert types
15. Raw security log monitoring table

# Technologies Used
1. Python
2. Pandas
3. Matplotlib
4. Requests
5. SMTP
6. Wireshark
7. Jupyter Notebook
8. Streamlit

# Detection Rules

# Host-Based Rules :
1. Brute Force Detection
2. Unusual Login Time Detection
3. Successful Login After Multiple Failures
4. High Activity IP Detection

# Network-Based Rules :
1. High Network Activity Detection
2. Suspicious Protocol Detection
3. Large Packet Detection

# Streamlit Dashboard
The Streamlit dashboard provides an interactive SOC-style monitoring interface with:

1. Total alert metrics
2. High severity alert metrics
3. Unique suspicious IP metrics
4. Alert type metrics
5. Recent security alerts table
6. Alert severity distribution chart
7. Traffic by hour chart
8. Top suspicious IPs chart
9. Most targeted usernames chart
10. Protocol usage distribution pie chart
11. Suspicious activity by country chart
12. Top alert types chart
13. Alerts by protocol chart
14. Raw security logs table
15. Sidebar filters for severity and protocol

# Visualizations
The project includes:

1. Alert count by severity
2. Alert count by type
3. Top suspicious IPs
4. Alerts by country
5. Protocol distribution
6. Traffic by hour
7. Most targeted usernames
8. Alert types distribution

# Project Structure

SIEM-Detection-System/
│
├── notebooks/
│   └── SIEM_device.ipynb
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── processed_siem_logs.csv
│   ├── auth.txt
│   ├── auth copy.txt
│   └── network_logs.csv
│
├── screenshots/
│   ├── dashboard_overview.png
│   ├── severity_distribution.png
│   └── protocol_distribution.png
│
├── README.md
└── requirements.txt

# Future Improvements
. Isolation Forest anomaly detection
. atabase integration
. Real-time packet capture integration
. Export alerts to CSV or PDF reports
. Dashboard login authentication
. Live dashboard refresh support
. Advanced filtering options

# requirements
. pandas
. matplotlib
. requests
. streamlit
