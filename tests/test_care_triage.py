import pytest
from care_triage import CareTriage, Ticket

@pytest.fixture
def care_triage():
    categories = ["Hardware", "Software", "Unknown"]
    routing_rules = {"Hardware": 1, "Software": 2}
    return CareTriage(categories, routing_rules)

def test_classify(care_triage):
    ticket = Ticket(1, "My hardware is broken")
    classified_ticket = care_triage.classify(ticket)
    assert classified_ticket.category == "Hardware"

def test_route(care_triage):
    ticket = Ticket(1, "My software is broken")
    ticket.category = "Software"
    routed_ticket = care_triage.route(ticket)
    assert routed_ticket.team_id == 2

def test_assign(care_triage):
    ticket = Ticket(1, "My hardware is broken")
    assigned_ticket = care_triage.assign(ticket)
    assert assigned_ticket.category == "Hardware"
    assert assigned_ticket.team_id == 1

def test_validate(care_triage):
    ticket = Ticket(1, "My hardware is broken")
    ticket.category = "Hardware"
    ticket.team_id = 1
    assert care_triage.validate(ticket) is True

def test_validate_invalid(care_triage):
    ticket = Ticket(1, "My hardware is broken")
    assert care_triage.validate(ticket) is False

def test_classify_unknown(care_triage):
    ticket = Ticket(1, "My unknown issue")
    classified_ticket = care_triage.classify(ticket)
    assert classified_ticket.category == "Unknown"
