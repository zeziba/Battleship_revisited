from dataclasses import dataclass
from enum import Enum, auto
import Fleet
import Board


class State(Enum):
    PERSON = auto()
    AI = auto()


@dataclass()
class Player:
    __state: State
    __board: Board.Board
    __fleet: Fleet.GeneralFleet

    @property
    def state(self) -> State:
        return self.__state

    @property
    def fleet(self) -> Fleet.GeneralFleet:
        return self.__fleet

    @property
    def board(self) -> Board.Board:
        return self.__board

    def place_fleet(self) -> None:
        if self.state is State.AI:
            self.fleet.generate()
        else:
            self.fleet.generate()

    @property
    def destroyed(self) -> bool:
        if self.fleet.fleet is None:
            return True
        return all(self.fleet.fleet[ship].is_sunk for ship in self.fleet.fleet)
