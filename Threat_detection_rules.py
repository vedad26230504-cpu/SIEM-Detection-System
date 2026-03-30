def detect_threats(parsed_logs):
    alerts = []

    from collections import defaultdict

    failed_attempts = defaultdict(int)
    total_activity = defaultdict(int)

    # First pass
    for entry in parsed_logs:
        ip = entry["ip"]
        event = entry["event"]
        hour = entry["hour"]

        total_activity[ip] += 1

        if event == "FAILED_LOGIN":
            failed_attempts[ip] += 1

        # 🌙 Time anomaly
        if event == "SUCCESS_LOGIN" and (hour < 6 or hour > 22):
            alerts.append({
                "type": "UNUSUAL_LOGIN_TIME",
                "ip": ip,
                "severity": "MEDIUM",
                "details": f"Login at hour {hour}"
            })

    # 🚨 Brute force
    for ip, count in failed_attempts.items():
        if count >= 5:
            alerts.append({
                "type": "BRUTE_FORCE",
                "ip": ip,
                "severity": "HIGH",
                "details": f"{count} failed attempts"
            })

    # ⚠️ Success after failure
    for entry in parsed_logs:
        ip = entry["ip"]
        if entry["event"] == "SUCCESS_LOGIN" and failed_attempts[ip] >= 5:
            alerts.append({
                "type": "POSSIBLE_COMPROMISE",
                "ip": ip,
                "severity": "HIGH",
                "details": "Successful login after multiple failures"
            })

    # 🟡 High activity
    for ip, count in total_activity.items():
        if count > 15:
            alerts.append({
                "type": "HIGH_ACTIVITY",
                "ip": ip,
                "severity": "MEDIUM",
                "details": f"{count} events detected"
            })

    return alerts
