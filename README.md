# Intelligent Alert Automation 🚨🤖

An intelligent automation system that validates CPU utilization alerts and automatically creates or resolves tickets, reducing noise and manual effort in monitoring operations.

## 🔍 Problem Statement
Traditional monitoring systems generate too many alerts, causing alert fatigue and unnecessary ticket creation.

## 💡 Solution
This project intelligently processes CPU utilization alerts using Python logic and configuration-based rules to:
- Validate alerts
- Avoid false positives
- Create tickets only when required
- Auto-resolve alerts when usage normalizes

## 🛠️ Tools & Technologies
- Python
- Linux
- Monitoring concepts
- ServiceNow (ticketing logic)
- Automation scripting

## ⚙️ How It Works
1. CPU utilization alert is received
2. Alert is validated against threshold rules
3. If valid → ticket is created
4. If usage returns to normal → ticket is auto-resolved

## ▶️ How to Run

```bash


