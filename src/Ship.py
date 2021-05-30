from dataclasses import dataclass, field, MISSING
from enum import Enum, auto, unique

import Board


@unique
class Direction(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()


@dataclass()
class Ship:
    name: field(default_factory=str)
    length: field(default_factory=int)

    def hit(self, px: int, py: int) -> bool:
        if (
            self.set_pos(px, py) in self.positions
            and not self.positions[self.set_pos(px, py)].hit
        ):
            self.positions[self.set_pos(px, py)].hit = True
            self.hit_points -= 1
            return True
        return False

    def place_ship(self, start_x: int, start_y: int, board: Board.Board) -> bool:
        if len(self.positions) == 0:
            h = 1 if self.directionality is Direction.HORIZONTAL else 0
            v = 0 if self.directionality is Direction.HORIZONTAL else 1
            for i in range(self.length):
                x = start_x + i * h
                y = start_y + i * v
                self.positions[self.set_pos(x, y)] = board.tiles_set(
                    x, y, Board.Tile.Tile(self, False)
                )
            return True
        return False

    @property
    def is_sunk(self) -> bool:
        return self.hit_points == 0

    @property
    def is_placed(self) -> bool:
        return len(self.positions) == self.length

    @staticmethod
    def set_pos(px, py) -> str:
        return f"{py},{px}"

    @property
    def directionality(self):
        return self.__directionality

    @directionality.setter
    def directionality(self, value: Direction):
        self.__directionality = value

    def __post_init__(self):
        self.__directionality: Direction.VERTICAL = field(default=Direction)
        self.hit_points = self.length
        self.positions = dict()
