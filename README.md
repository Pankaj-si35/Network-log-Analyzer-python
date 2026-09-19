# Network-log-Analyzer-python
A Python-based Network Log Analyzer for parsing authentication logs, detecting failed login attempts, identifying suspicious IP addresses, and generating structured CSV reports and security visualizations
# 🔐 Network Log Analyzer using Python

## 📌 Project Overview

Network Log Analyzer is a Python-based cybersecurity tool designed to analyze authentication and network log files, detect failed login attempts, identify suspicious IP addresses, and generate structured security reports.

The project demonstrates how Python can be used for basic Security Operations Center (SOC) activities such as log analysis, suspicious activity detection, data processing, and security visualization.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze authentication log files automatically.
- Detect failed login attempts.
- Extract IP addresses associated with failed logins.
- Count failed login attempts for each IP address.
- Identify potentially suspicious IP addresses.
- Generate a structured CSV security report.
- Visualize suspicious login activity using a bar chart.
- Demonstrate practical Python usage in cybersecurity.

---

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (`re`)
- Pandas
- Matplotlib
- Collections / `defaultdict`
- CSV
- Authentication Log Files

---

## 📂 Project Structure

```text
Network-Log-Analyzer/
│
├── analyzer.py
├── auth.log
├── report.csv
└── screenshot.png  File Description
analyzer.py
Main Python program responsible for reading and analyzing the authentication log.
auth.log
Sample authentication log containing successful and failed login attempts.
report.csv
Automatically generated report containing IP addresses and their failed login counts.
screenshot.png
Project execution and visualization evidence.
⚙️ How the Project Works
The analyzer follows these steps:
1. Read the Log File
The Python script reads the auth.log file line by line.
2. Detect Failed Login Attempts
A Regular Expression pattern searches for log entries containing:
Failed password
3. Extract IP Addresses
The IP address associated with each failed login attempt is extracted from the log entry.
4. Count Failed Attempts
The program maintains a counter for every IP address.
Example:
192.168.1.10 → 4 failed attempts
192.168.1.11 → 1 failed attempt
192.168.1.12 → 1 failed attempt
5. Identify Suspicious IP Addresses
IPs with more than two failed login attempts are flagged as suspicious.
Example:
192.168.1.10 → 4 failed attempts
This can indicate repeated authentication failures and may require further investigation.
Note: A failed-login threshold alone does not prove that an IP address is malicious. It is only a basic detection rule for this project.
6. Generate CSV Report
The analyzed results are exported into:
report.csv
7. Generate Visualization
Matplotlib is used to create a bar chart showing failed login attempts by IP address.
📊 Sample Analysis
The sample log produced the following result:
IP Address
Failed Attempts
192.168.1.10
4
192.168.1.11
1
192.168.1.12
1
The project identifies:
Suspicious IP:
192.168.1.10
Failed Attempts: 4
📈 Visualization
The project generates a bar chart representing the number of failed login attempts associated with each IP address.
This visualization makes it easier to identify IP addresses generating a higher number of authentication failures.
🚀 Installation
Clone the repository:
git clone https://github.com/YOUR-USERNAME/network-log-analyzer-python.git
Move into the project directory:
cd network-log-analyzer-python
Install the required Python libraries:
pip install pandas matplotlib
▶️ Usage
Run the analyzer:
python analyzer.py
The program will:
Read auth.log
Detect failed login attempts
Extract IP addresses
Count failed attempts
Identify suspicious IPs
Generate report.csv
Display the security visualization
🔍 Example Log Entry
Example authentication log:
Jun 19 10:12:23 server sshd[2455]: Failed password for root from 192.168.1.10 port 22
The analyzer extracts:
IP Address: 192.168.1.10
Event: Failed Login
🔐 Cybersecurity Use Case
Log analysis is an important activity in cybersecurity and Security Operations Center (SOC) environments.
This project demonstrates a simplified version of:
Authentication monitoring
Failed-login detection
IP-based activity analysis
Security event processing
Basic threat detection
Automated security reporting
📚 Skills Demonstrated
Through this project, the following practical skills were applied:
Python programming
File handling
Regular Expressions
Log analysis
Data processing
CSV reporting
Data visualization
Basic security monitoring
Suspicious activity detection
🔮 Future Improvements
Future versions of this project can include:
Real-time log monitoring
Automatic alert generation
Email notifications
GeoIP-based IP location analysis
Login success/failure correlation
Brute-force detection
Configurable detection thresholds
Multiple log format support
Web-based dashboard
SQLite database integration
SIEM integration
Machine-learning-based anomaly detection
⚠️ Disclaimer
This project is created for educational and cybersecurity learning purposes.
The sample logs used in this project are simulated/local data. Detection results should not be treated as proof that an IP address is malicious.
👨‍💻 Author
Your Name
Cybersecurity Enthusiast | Python | Network Security | SOC | AI Security
⭐ Project Highlights
🐍 Python-based security automation
🔎 Authentication log analysis
🚨 Suspicious IP detection
📊 Automated CSV reporting
📈 Security visualization
🔐 Practical cybersecurity project
