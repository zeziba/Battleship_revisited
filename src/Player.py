from dataclasses import dataclass
from enum import Enum

import Board


class PlayerType(Enum):
    PLAYER: 0
    COMPUTER: 1

    def __str__(self):
        return f"{self.name}"


@dataclass()
class Player:
    type: PlayerType
    board: Board.Board
