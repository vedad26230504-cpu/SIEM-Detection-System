# Alert Count by Severity
import matplotlib.pyplot as plt
from collections import Counter

severity_counts = Counter(alert['severity'] for alert in all_alerts)

plt.figure(figsize=(6,4))
bars = plt.bar(severity_counts.keys(), severity_counts.values())

plt.title("Alert Count by Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Alerts")

# Add numbers on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha='center',
        va='bottom'
    )

plt.show()



# Alert Count by Type
type_counts = Counter(alert['type'] for alert in all_alerts)

plt.figure(figsize=(10,5))
bars = plt.bar(type_counts.keys(), type_counts.values())

plt.title("Alert Count by Type")
plt.xlabel("Alert Type")
plt.ylabel("Number of Alerts")
plt.xticks(rotation=45)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha='center',
        va='bottom'
    )

plt.show()



# Top 10 Suspicious IPs
from collections import Counter
import matplotlib.pyplot as plt

ip_counts = Counter(alert['ip'] for alert in all_alerts if alert['ip'] != "N/A")
top_ips = dict(ip_counts.most_common(10))

plt.figure(figsize=(10,5))
bars = plt.bar(top_ips.keys(), top_ips.values())

plt.title("Top 10 Suspicious IPs")
plt.xlabel("IP Address")
plt.ylabel("Number of Alerts")
plt.xticks(rotation=45)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha='center',
        va='bottom'
    )

plt.show()



# Alerts by Country
from collections import Counter
import matplotlib.pyplot as plt
countries = []

for alert in all_alerts:
    if alert["ip"] != "N/A":
        countries.append(get_country(alert["ip"]))

country_counts = Counter(countries)

plt.figure(figsize=(8,8))
plt.pie(
    country_counts.values(),
    labels=country_counts.keys(),
    autopct='%1.1f%%'
)

plt.title("Alerts by Country")
plt.show()
