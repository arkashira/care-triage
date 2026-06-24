import pytest
import json
from routing import Ticket, Queue, load_routing_rules, route_ticket, log_routing_decision, main

def test_load_routing_rules(tmp_path):
    # Create a temporary routing rules file
    file_path = tmp_path / 'routing_rules.json'
    routing_rules = {
        'queue1': [{'name': 'queue1', 'priority': 'high', 'skill_set': 'python'}],
        'queue2': [{'name': 'queue2', 'priority': 'low', 'skill_set': 'java'}]
    }
    with open(file_path, 'w') as file:
        json.dump(routing_rules, file)
    
    loaded_rules = load_routing_rules(str(file_path))
    assert isinstance(loaded_rules, dict)

def test_route_ticket():
    ticket = Ticket(1, 'high', 'python')
    routing_rules = {
        'queue1': [Queue('queue1', 'high', 'python')],
        'queue2': [Queue('queue2', 'low', 'java')]
    }
    queue_name = route_ticket(ticket, routing_rules)
    assert queue_name == 'queue1'

def test_log_routing_decision(capsys):
    ticket = Ticket(1, 'high', 'python')
    log_routing_decision(ticket, 'queue1')
    captured = capsys.readouterr()
    assert "Ticket 1 routed to queue1" in captured.out

def test_main(tmp_path):
    # Create a temporary routing rules file
    file_path = tmp_path / 'routing_rules.json'
    routing_rules = {
        'queue1': [{'name': 'queue1', 'priority': 'high', 'skill_set': 'python'}],
        'queue2': [{'name': 'queue2', 'priority': 'low', 'skill_set': 'java'}]
    }
    with open(file_path, 'w') as file:
        json.dump(routing_rules, file)
    
    ticket = Ticket(1, 'high', 'python')
    queue_name = main(str(file_path), ticket)
    assert queue_name == 'queue1'

def test_main_no_matching_queue(tmp_path):
    # Create a temporary routing rules file
    file_path = tmp_path / 'routing_rules.json'
    routing_rules = {
        'queue1': [{'name': 'queue1', 'priority': 'high', 'skill_set': 'python'}],
        'queue2': [{'name': 'queue2', 'priority': 'low', 'skill_set': 'java'}]
    }
    with open(file_path, 'w') as file:
        json.dump(routing_rules, file)
    
    ticket = Ticket(1, 'high', 'ruby')
    with pytest.raises(ValueError):
        main(str(file_path), ticket)
