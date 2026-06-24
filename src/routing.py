import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Ticket:
    id: int
    priority: str
    skill_set: str

@dataclass
class Queue:
    name: str
    priority: str
    skill_set: str

def load_routing_rules(file_path: str) -> Dict[str, List[Queue]]:
    try:
        with open(file_path, 'r') as file:
            routing_rules = json.load(file)
            # Convert the loaded JSON into Queue objects
            converted_rules = {}
            for queue_name, queues in routing_rules.items():
                converted_queues = [Queue(queue['name'], queue['priority'], queue['skill_set']) for queue in queues]
                converted_rules[queue_name] = converted_queues
            return converted_rules
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}

def route_ticket(ticket: Ticket, routing_rules: Dict[str, List[Queue]]) -> str:
    for queue_name, queues in routing_rules.items():
        for queue in queues:
            if ticket.priority == queue.priority and ticket.skill_set == queue.skill_set:
                return queue_name
    return None

def log_routing_decision(ticket: Ticket, queue_name: str) -> None:
    print(f"Ticket {ticket.id} routed to {queue_name}")

def main(file_path: str, ticket: Ticket) -> str:
    routing_rules = load_routing_rules(file_path)
    queue_name = route_ticket(ticket, routing_rules)
    if queue_name:
        log_routing_decision(ticket, queue_name)
        return queue_name
    else:
        raise ValueError("No matching queue found")
