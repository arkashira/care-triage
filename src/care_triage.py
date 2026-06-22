import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Ticket:
    id: int
    description: str
    symptoms: List[str]

@dataclass
class KnowledgeBase:
    root_causes: Dict[str, List[str]]

class CareTriage:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.knowledge_base = knowledge_base

    def suggest_root_cause(self, ticket: Ticket) -> str:
        for symptom in ticket.symptoms:
            if symptom in self.knowledge_base.root_causes:
                return self.knowledge_base.root_causes[symptom][0]
        return "Unknown"

    def generate_suggestions(self, tickets: List[Ticket]) -> Dict[int, str]:
        suggestions = {}
        for ticket in tickets:
            suggestion = self.suggest_root_cause(ticket)
            suggestions[ticket.id] = suggestion
        return suggestions

def load_knowledge_base(json_data: str) -> KnowledgeBase:
    data = json.loads(json_data)
    root_causes = {symptom: causes for symptom, causes in data.items()}
    return KnowledgeBase(root_causes)

def main():
    knowledge_base_json = '''
    {
        "headache": ["Migraine", "Tension"],
        "fever": ["Infection", "Viral"]
    }
    '''
    knowledge_base = load_knowledge_base(knowledge_base_json)
    care_triage = CareTriage(knowledge_base)

    ticket1 = Ticket(1, "Patient has a headache", ["headache"])
    ticket2 = Ticket(2, "Patient has a fever", ["fever"])
    tickets = [ticket1, ticket2]

    suggestions = care_triage.generate_suggestions(tickets)
    print(suggestions)

if __name__ == "__main__":
    main()
