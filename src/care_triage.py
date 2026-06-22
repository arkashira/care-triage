import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Ticket:
    score: int
    metadata: dict

@dataclass
class Agent:
    skill_tags: List[str]

class CareTriage:
    def __init__(self, marketplace_api):
        self.marketplace_api = marketplace_api

    def suggest_agent(self, ticket: Ticket) -> Optional[Agent]:
        if ticket.score > 70:
            available_agents = self.marketplace_api.query_agents(ticket.metadata.get('skill_tags', []))
            if available_agents:
                return available_agents[0]
        return None

    def assign_agent(self, ticket: Ticket, agent: Agent) -> None:
        ticket.metadata['assigned_agent'] = agent.skill_tags
        print(f"Assigned agent with skill tags {agent.skill_tags} to ticket")

    def notify_ops_manager(self, ticket: Ticket) -> None:
        print(f"No agents available for ticket with score {ticket.score}")

class MarketplaceAPI:
    def query_agents(self, skill_tags: List[str]) -> List[Agent]:
        # Simulate a query to the marketplace API
        available_agents = [
            Agent(skill_tags=['tag1', 'tag2']),
            Agent(skill_tags=['tag3', 'tag4'])
        ]
        return [agent for agent in available_agents if any(tag in skill_tags for tag in agent.skill_tags)]

def main():
    marketplace_api = MarketplaceAPI()
    care_triage = CareTriage(marketplace_api)

    ticket = Ticket(score=80, metadata={'skill_tags': ['tag1', 'tag3']})
    agent = care_triage.suggest_agent(ticket)
    if agent:
        care_triage.assign_agent(ticket, agent)
    else:
        care_triage.notify_ops_manager(ticket)

if __name__ == '__main__':
    main()
