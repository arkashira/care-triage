import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class CareTriageSystem:
    instructions: str
    guidance: str

    def provide_instructions(self):
        return self.instructions

    def provide_guidance(self):
        return self.guidance

    def validate_input(self, input_data):
        if not isinstance(input_data, dict):
            raise ValueError("Input must be a dictionary")
        if "user_input" not in input_data:
            raise ValueError("Input must contain 'user_input' key")
        return input_data["user_input"]

    def process_input(self, input_data):
        try:
            user_input = self.validate_input(input_data)
            return f"Processing input: {user_input}"
        except ValueError as e:
            return f"Error: {str(e)}"

def main():
    parser = ArgumentParser(description="Care Triage System")
    parser.add_argument("--instructions", help="Instructions for the system")
    parser.add_argument("--guidance", help="Guidance for the system")
    args = parser.parse_args()

    system = CareTriageSystem(args.instructions, args.guidance)
    print(system.provide_instructions())
    print(system.provide_guidance())

    input_data = {"user_input": "example input"}
    print(system.process_input(input_data))

if __name__ == "__main__":
    main()
