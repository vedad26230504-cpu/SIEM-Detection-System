parsed_logs = []

for log in logs:
    log = log.strip()
    
    # Skip empty lines
    if not log:
        continue

    import re
    
    # Extract IP
    ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', log)
    ip = ip_match.group() if ip_match else None

    parts = log.split()

    # Safety check
    if len(parts) < 3:
        continue

    # Extract timestamp
    timestamp = " ".join(parts[:3])

    # Extract hour
    hour = int(parts[2].split(":")[0])

    # Event type
    if "Failed password" in log:
        event = "FAILED_LOGIN"
    elif "Accepted password" in log:
        event = "SUCCESS_LOGIN"
    else:
        event = "OTHER"

    parsed_logs.append({
        "ip": ip,
        "event": event,
        "timestamp": timestamp,
        "hour": hour
    })

parsed_logs
