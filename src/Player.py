from dataclasses import dataclass
from enum import Enum, auto
import Fleet
import Board


class State(Enum):
    PERSON: auto()
    AI: auto()


@dataclass()
class Player:
    __state: State
    __board: Board.Board
    __fleet: Fleet.GeneralFleet

    @property
    def state(self):
        return self.__state

    @property
    def fleet(self):
        return self.__fleet

    @property
    def board(self):
        return self.__board

    def place_fleet(self):
        if self.state is State.AI:
            self.fleet.generate()
        else:
            self.fleet.place_fleet()
