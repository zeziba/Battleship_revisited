from dataclasses import dataclass
from enum import Enum, auto

import Ship
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
            self.__fleet[ship] = Ship.Ship(ship.name, FLEET[ship])

    def place_fleet(self):
        self.__fleet = dict()
        for ship in list(Fleet):
            # TODO: Once UI layer is give control and get coords of ship placement
            # TODO: Finish testing of this method
            pass

    def hit(self, px, py) -> bool:
        for ship in self.fleet:
            if self.fleet[ship].hit(px, py):
                return True
        return False
