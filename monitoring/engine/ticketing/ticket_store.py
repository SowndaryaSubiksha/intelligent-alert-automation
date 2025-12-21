import json
import uuid
from datetime import datetime

TICKET_DB = "data/tickets.json"

def load_tickets():
    try:
        with open(TICKET_DB, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_ticket(ticket):
    tickets = load_tickets()
    tickets.append(ticket)
    with open(TICKET_DB, "w") as f:
        json.dump(tickets, f, indent=2)

def create_ticket(cpu_usage):
    """
    Creates a new ticket when CPU usage is high
    """
    ticket = {
        "id": str(uuid.uuid4())[:8],
        "issue": "High CPU Usage",
        "value": cpu_usage,
        "status": "OPEN",
        "created_at": datetime.now().isoformat()
    }
    save_ticket(ticket)
    return ticket["id"]
