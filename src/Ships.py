from dataclasses import dataclass
from enum import Enum


class ShipType(Enum):
    BATTLESHIP = 0
    CARRIER = 1
    PATROL_BOAT = 2
    SUBMARINE = 3
    DESTROYER = 4

    def __str__(self):
        return f"{self.name}"


Lengths = {
    ShipType.BATTLESHIP: 4,
    ShipType.CARRIER: 5,
    ShipType.PATROL_BOAT: 2,
    ShipType.SUBMARINE: 3,
    ShipType.DESTROYER: 3,
}


@dataclass(frozen=True, order=True)
class Ship:
    type: ShipType
    length: int
    positions: list
