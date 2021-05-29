from dataclasses import dataclass
from enum import Enum, auto
from random import choice

from Ship import Ship, Direction
import src.GameRules


Fleet = Enum("Fleet", {name: auto() for name in src.GameRules.FLEET})
FLEET = {ship: src.GameRules.FLEET[ship.name] for ship in list(Fleet)}


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
