from dataclasses import dataclass
from enum import Enum, auto


SIZE = 100


class TileType(Enum):
    EMPTY = auto()
    FULL = auto()
    HIT = auto()


@dataclass()
class Board:
    board: tuple[TileType]
