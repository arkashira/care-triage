from care_triage import Ticket, KnowledgeBase, CareTriage, load_knowledge_base

def test_suggest_root_cause():
    knowledge_base_json = '''
    {
        "headache": ["Migraine", "Tension"],
        "fever": ["Infection", "Viral"]
    }
    '''
    knowledge_base = load_knowledge_base(knowledge_base_json)
    care_triage = CareTriage(knowledge_base)

    ticket = Ticket(1, "Patient has a headache", ["headache"])
    suggestion = care_triage.suggest_root_cause(ticket)
    assert suggestion == "Migraine"

def test_generate_suggestions():
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
    assert suggestions == {1: "Migraine", 2: "Infection"}

def test_load_knowledge_base():
    knowledge_base_json = '''
    {
        "headache": ["Migraine", "Tension"],
        "fever": ["Infection", "Viral"]
    }
    '''
    knowledge_base = load_knowledge_base(knowledge_base_json)
    assert knowledge_base.root_causes == {"headache": ["Migraine", "Tension"], "fever": ["Infection", "Viral"]}

def test_suggest_root_cause_unknown():
    knowledge_base_json = '''
    {
        "headache": ["Migraine", "Tension"],
        "fever": ["Infection", "Viral"]
    }
    '''
    knowledge_base = load_knowledge_base(knowledge_base_json)
    care_triage = CareTriage(knowledge_base)

    ticket = Ticket(1, "Patient has a cough", ["cough"])
    suggestion = care_triage.suggest_root_cause(ticket)
    assert suggestion == "Unknown"
