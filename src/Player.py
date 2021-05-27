from dataclasses import dataclass
from enum import Enum, auto
import src.Board as Board


class PlayerType(Enum):
    PLAYER = auto()
    COMPUTER = auto()

    def __str__(self):
        return f"{self.name}"


@dataclass()
class Player:
    type: PlayerType
    board: Board.Board
