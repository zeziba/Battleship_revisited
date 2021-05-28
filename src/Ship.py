from dataclasses import dataclass, field
from enum import Enum, auto, unique


@unique
class Direction(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()


@dataclass()
class Ship:
    name: field(default_factory=str)
    length: field(default_factory=int)
    directionality: field(default=Direction)

    def hit(self, px: int, py: int) -> bool:
        if (
                self.set_pos(px, py) in self.positions
                and self.positions[self.set_pos(px, py)] == 0
        ):
            self.positions[self.set_pos(px, py)] = 1
            self.hit_points -= 1
            return True
        return False

    def place_ship(self, start_x: int, start_y: int) -> bool:
        if len(self.positions) == 0:
            v = 1 if self.directionality is Direction.VERTICAL else 0
            h = 1 if self.directionality is Direction.HORIZONTAL else 0
            for i in range(self.length):
                self.positions[self.set_pos(start_x + i * h, start_y + i * v)] = 0
            return True
        return False

    @property
    def is_sunk(self) -> bool:
        return self.hit_points == 0

    @staticmethod
    def set_pos(px, py):
        return f"{py},{px}"

    def __post_init__(self):
        self.hit_points = self.length
        self.positions = dict()
