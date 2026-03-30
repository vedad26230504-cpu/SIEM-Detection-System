with open("/Users/akshatchaturvedi/Desktop/siem_project/auth.txt", "r") as file:
    logs = file.readlines()

# Print each log line
for log in logs:
    print(log.strip())
