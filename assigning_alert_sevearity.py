for alert in alerts:
    country = get_country(alert["ip"])
    print(f"[{alert['severity']}] {alert['type']} from {alert['ip']} ({country}) → {alert['details']}")

alerts = []

# Brute force detection (HIGH)
for ip, count in failed_attempts.items():
    if count >= 5:
        alerts.append({
            "type": "BRUTE_FORCE",
            "ip": ip,
            "severity": "HIGH",
            "details": f"{count} failed attempts"
        })

# Time-based anomaly (MEDIUM)
for entry in parsed_logs:
    if entry["event"] == "SUCCESS_LOGIN":
        if entry["hour"] < 6 or entry["hour"] > 22:
            alerts.append({
                "type": "UNUSUAL_LOGIN_TIME",
                "ip": entry["ip"],
                "severity": "MEDIUM",
                "details": f"Login at {entry['timestamp']}"
            })

# Print all alerts
for alert in alerts:
    country = get_country(alert["ip"])
    print(f"[{alert['severity']}] {alert['type']} from {alert['ip']} ({country}) → {alert['details']}")
