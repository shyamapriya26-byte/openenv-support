from dataclasses import dataclass

@dataclass
class Observation:
    issue: str
    current_step: int
    steps_taken: int

@dataclass
class Action:
    name: str