# SIEM-Detection-System

# Project Overview
This project is a SIEM-like security monitoring system built in Python to simulate a real SOC workflow. It processes authentication logs, applies multiple rule-based detection techniques to identify suspicious activity such as brute force attacks, unusual login times, high activity IPs, and potential account compromise, and enriches alerts with GeoIP information. The system also integrates Wireshark network traffic analysis to detect suspicious protocols, abnormal packet sizes, and unusual traffic patterns. High severity alerts are automatically escalated through email notifications, and the project includes visualizations to analyze alert trends, suspicious IPs, protocols, and attack origins.

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

  
# Technologies Used
1. Python
2. Pandas
3. Matplotlib
4. Requests
5. SMTP
6. Wireshark
7. Jupyter Notebook

   
# Detection Rules

# Host-Based Rules :
1. Brute Force Detection
2. Unusual Login Time Detection
3. Successful Login After Multiple Failures
4. High Activity IP Detection   
#  Network-Based Rules :
1. High Network Activity Detection
2. Suspicious Protocol Detection
3. Large Packet Detection

# Visualizations
The project includes:

1. Alert count by severity
2. Alert count by type
3. Top suspicious IPs
4. Alerts by country
5. Protocol distribution

# Future Improvements
. Streamlit dashboad
. Isolation Forest anomaly detection
. Database integration
. Real-time packet capture integration
. Export alerts to CSV or PDF reports


# requirements.txt Content
. pandas
. matplotlib
. requests
