from care_triage import CareTriage, Ticket, Agent, MarketplaceAPI

def test_suggest_agent():
    marketplace_api = MarketplaceAPI()
    care_triage = CareTriage(marketplace_api)

    ticket = Ticket(score=80, metadata={'skill_tags': ['tag1', 'tag3']})
    agent = care_triage.suggest_agent(ticket)
    assert agent is not None
    assert agent.skill_tags == ['tag1', 'tag2']

def test_suggest_agent_no_available_agents():
    marketplace_api = MarketplaceAPI()
    care_triage = CareTriage(marketplace_api)

    ticket = Ticket(score=80, metadata={'skill_tags': ['tag5', 'tag6']})
    agent = care_triage.suggest_agent(ticket)
    assert agent is None

def test_assign_agent():
    marketplace_api = MarketplaceAPI()
    care_triage = CareTriage(marketplace_api)

    ticket = Ticket(score=80, metadata={'skill_tags': ['tag1', 'tag3']})
    agent = Agent(skill_tags=['tag1', 'tag2'])
    care_triage.assign_agent(ticket, agent)
    assert ticket.metadata['assigned_agent'] == ['tag1', 'tag2']

def test_notify_ops_manager():
    marketplace_api = MarketplaceAPI()
    care_triage = CareTriage(marketplace_api)

    ticket = Ticket(score=80, metadata={'skill_tags': ['tag5', 'tag6']})
    care_triage.notify_ops_manager(ticket)
    # No assertion, just verify that the method runs without errors
