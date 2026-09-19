import re
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: File path
log_file = "auth.log"

# Step 2: Regex pattern to find failed logins
pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

# Step 3: Dictionary for counting failed attempts
failed_attempts = defaultdict(int)

# Step 4: Read the log file and extract IP addresses
with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

# Step 5: Print all failed attempts
print("🔹 Failed Login Attempts by IP:\n")
for ip, count in failed_attempts.items():
    print(f"{ip} --> {count} times")

# Step 6: Detect and print suspicious IPs
print("\n🚨 Suspicious IPs (more than 2 failed attempts):")
suspicious_ips = {ip: count for ip, count in failed_attempts.items() if count > 2}
if suspicious_ips:
    for ip, count in suspicious_ips.items():
        print(f"⚠ {ip} - {count} failed logins")
else:
    print("No suspicious IPs found ✅")

# Step 7: Save report to CSV
df = pd.DataFrame(failed_attempts.items(), columns=["IP Address", "Failed Attempts"])
df.to_csv("report.csv", index=False)
print("\n📁 Report saved as 'report.csv'")

# Step 8: Show top 3 most suspicious IPs
if len(df) > 0:
    top_ips = df.sort_values(by="Failed Attempts", ascending=False).head(3)
    print("\n🏆 Top 3 Most Suspicious IPs:")
    for index, row in top_ips.iterrows():
        print(f"{row['IP Address']} - {row['Failed Attempts']} failed attempts")

# Step 9: Visualize results
plt.figure(figsize=(8, 5))
plt.bar(df["IP Address"], df["Failed Attempts"], color="orange", edgecolor="black")
plt.xlabel("IP Address")
plt.ylabel("Failed Login Attempts")
plt.title("Network Log Analyzer Report")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 10 (Optional): Time-based analysis (for advanced feature)
# You can extract timestamps if needed later