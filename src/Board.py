from dataclasses import dataclass
from enum import Enum


class TileType(Enum):
    EMPTY: 0
    FULL: 1
    HIT: 2


@dataclass()
class Board:
    board: tuple
