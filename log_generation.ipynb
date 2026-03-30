# log generation 
import random

ips = [
    "192.168.1.10",  # internal
    "10.0.0.5",
    "172.16.0.8",
    "203.0.113.5",   # external attacker
    "8.8.8.8"        # normal public
]

users = ["admin", "root", "guest", "user"]

logs = []

for i in range(100):  # generate 100 logs
    ip = random.choice(ips)
    user = random.choice(users)
    
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    timestamp = f"Mar 27 {hour:02d}:{minute:02d}:{second:02d}"

    if random.random() < 0.7:
        log = f"{timestamp} server sshd[{1000+i}]: Failed password for invalid user {user} from {ip} port 22 ssh2"
    else:
        log = f"{timestamp} server sshd[{1000+i}]: Accepted password for user from {ip} port 22 ssh2"

    logs.append(log)

# Save to file
with open("auth.txt", "w") as f:
    for log in logs:
        f.write(log + "\n")
print("Generated 100 logs")





# prase the generated logs 

import re

parsed_logs = []

for log in logs:
    # Extract IP address
    ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', log)
    ip = ip_match.group() if ip_match else None

    # Identify event type
    if "Failed password" in log:
        event = "FAILED_LOGIN"
    elif "Accepted password" in log:
        event = "SUCCESS_LOGIN"
    else:
        event = "OTHER"

    parsed_logs.append({
        "ip": ip,
        "event": event
    })

parsed_logs
