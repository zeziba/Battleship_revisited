from enum import Enum, auto

SIZE = 10


def check_xy(x, y) -> bool:
    """Checks if the x, y coords fall within the board"""
    size = SIZE - 1
    return (size >= x >= 0) and (size >= y >= 0)


FLEET = {
    "CARRIER": 5,
    "BATTLESHIP": 4,
    "PATROLBOAT": 2,
    "SUBMARINE": 3,
    "DESTROYER": 3,
}

OUTPUTS = (
    "Please enter in your coords: x y\n\t",
    "Please enter in your directionality: h -> horizontal or v -> vertical\n\t",
    "Please enter in the starting location of the {}: x y\n\t",
    "Placing {}",
    "Failed to place {} at ({}, {}) with directionality {} as not a valid location.",
)


class State(Enum):
    RUNNING = auto()
    STOPPED = auto()
