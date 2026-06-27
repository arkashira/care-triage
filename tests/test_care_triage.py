from care_triage import CareTriageSystem

def test_provide_instructions():
    system = CareTriageSystem("example instructions", "example guidance")
    assert system.provide_instructions() == "example instructions"

def test_provide_guidance():
    system = CareTriageSystem("example instructions", "example guidance")
    assert system.provide_guidance() == "example guidance"

def test_validate_input_valid():
    system = CareTriageSystem("example instructions", "example guidance")
    input_data = {"user_input": "example input"}
    assert system.validate_input(input_data) == "example input"

def test_validate_input_invalid_type():
    system = CareTriageSystem("example instructions", "example guidance")
    input_data = "example input"
    try:
        system.validate_input(input_data)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Input must be a dictionary"

def test_validate_input_missing_key():
    system = CareTriageSystem("example instructions", "example guidance")
    input_data = {"other_key": "example input"}
    try:
        system.validate_input(input_data)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Input must contain 'user_input' key"

def test_process_input_valid():
    system = CareTriageSystem("example instructions", "example guidance")
    input_data = {"user_input": "example input"}
    assert system.process_input(input_data) == "Processing input: example input"

def test_process_input_invalid():
    system = CareTriageSystem("example instructions", "example guidance")
    input_data = "example input"
    assert system.process_input(input_data) == "Error: Input must be a dictionary"
