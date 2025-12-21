import yaml
import logging

from monitoring.system_metrics import get_cpu_usage
from engine.decision_engine import decide_action
from ticketing.ticket_store import create_ticket

# Load configuration
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Configure logging
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    cpu_usage = get_cpu_usage()
    decision = decide_action(cpu_usage, config)

    logging.info(f"CPU Usage: {cpu_usage}%")
    logging.info(f"Decision taken: {decision}")

    if decision == "CREATE_TICKET":
        ticket_id = create_ticket(cpu_usage)
        print(f"Ticket created: {ticket_id}")
    elif decision == "IGNORE":
        print("CPU normal. Alert ignored.")
    else:
        print("CPU under observation.")

if __name__ == "__main__":
    main()
