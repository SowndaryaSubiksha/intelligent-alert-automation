Intelligent Alert Automation

📌 Overview
This project is a Python-based automation system designed to monitor system CPU usage, intelligently validate alerts, and automatically create tickets when required.  
It focuses on reducing false alerts and minimizing manual operational effort using only free and open-source tools.

---

🎯 Problem Statement
In many IT environments, monitoring tools generate frequent alerts, including false positives.  
This leads to unnecessary ticket creation, manual verification effort, and slower incident response.

---

 Solution
This project implements an intelligent alert validation workflow that:
1. Monitors real-time CPU usage
2. Applies configurable decision logic
3. Creates tickets only when thresholds are breached
4. Stores tickets locally for tracking and audit

---

🧠 Key Features
- Real-time CPU monitoring
- Decision-based alert validation
- Automated ticket creation
- Config-driven thresholds
- Modular project structure
- Lightweight JSON-based ticket storage

---

🛠️ Technologies Used
- Python  
- psutil  
- YAML  
- JSON  
- Logging  
- Git & GitHub  

---

📂 Project Structure

intelligent-alert-automation/
├── data/
├── engine/
├── monitoring/
├── ticketing/
├── main.py
├── config.yaml
├── requirements.txt
└── README.md


---

🔄 Workflow
1. CPU usage is collected using system metrics
2. Alert data is validated against thresholds
3. Decision engine determines the action:
   - Ignore alert
   - Continue monitoring
   - Create a ticket
4. Ticket details are stored locally
5. All actions are logged

---

▶️ How to Run
bash
pip install -r requirements.txt
python main.py


📈 Learning Outcomes

Python automation design

Monitoring fundamentals

Decision-based logic

Modular project structuring

Real-world automation use case


🚀 Future Enhancements

Memory and disk monitoring

Auto-resolution of tickets

Scheduling using cron

Notifications (email/Slack)

Unit testing


👩‍💻 Author

Sowndarya Subiksha
Python Automation | Monitoring | DevOps Fundamentals
