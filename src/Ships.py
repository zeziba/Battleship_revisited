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
    ShipType.Battleship: 4,
    ShipType.Carrier: 5,
    ShipType.PatrolBoat: 2,
    ShipType.Submarine: 3,
    ShipType.Destroyer: 3,
}


@dataclass(frozen=True, order=True)
class Ship:
    type: ShipType
    length: int
    positions: list
