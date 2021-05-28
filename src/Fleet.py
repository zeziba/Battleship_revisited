from dataclasses import dataclass
from enum import Enum, auto, unique
from random import choice

from Ship import Ship, Direction


@unique
class Fleet(Enum):
    CARRIER = auto()
    BATTLESHIP = auto()
    PATROLBOAT = auto()
    SUBMARINE = auto()
    DESTROYER = auto()


FLEET = {
    Fleet.CARRIER: 5,
    Fleet.BATTLESHIP: 4,
    Fleet.PATROLBOAT: 2,
    Fleet.SUBMARINE: 3,
    Fleet.DESTROYER: 3,
}


@dataclass
class GeneralFleet:
    __fleet = dict()

    @property
    def fleet(self) -> dict:
        return self.__fleet

    def generate(self) -> None:
        self.__fleet = dict()
        for ship in list(Fleet):
            # Random directionality choice for now
            self.__fleet[ship] = Ship(ship.name, FLEET[ship], choice(list(Direction)))

    def place_fleet(self):
        self.__fleet = dict()
        for ship in list(Fleet):
            # TODO: Once UI layer is give control and get coords of ship placement
            # TODO: Finish testing of this method
            pass
