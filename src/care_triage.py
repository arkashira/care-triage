import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Ticket:
    id: int
    text: str
    category: str = None
    team_id: int = None

class CareTriage:
    def __init__(self, categories: List[str], routing_rules: Dict[str, int]):
        self.categories = categories
        self.routing_rules = routing_rules
        self.model = self._train_model()

    def _train_model(self):
        # Simple mock model for demonstration purposes
        def model(text: str) -> str:
            if "hardware" in text:
                return "Hardware"
            elif "software" in text:
                return "Software"
            else:
                return "Unknown"
        return model

    def classify(self, ticket: Ticket) -> Ticket:
        category = self.model(ticket.text)
        if category not in self.categories:
            category = "Unknown"
        ticket.category = category
        return ticket

    def route(self, ticket: Ticket) -> Ticket:
        team_id = self.routing_rules.get(ticket.category)
        if team_id is not None:
            ticket.team_id = team_id
        return ticket

    def assign(self, ticket: Ticket) -> Ticket:
        ticket = self.classify(ticket)
        ticket = self.route(ticket)
        return ticket

    def validate(self, ticket: Ticket) -> bool:
        if ticket.category is None or ticket.team_id is None:
            return False
        return True
