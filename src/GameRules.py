from enum import Enum, auto

SIZE = 10

FLEET = {
    "CARRIER": 5,
    "BATTLESHIP": 4,
    "PATROLBOAT": 2,
    "SUBMARINE": 3,
    "DESTROYER": 3,
}

class State(Enum):
    RUNNING = auto()
    STOPPED = auto()
