from dataclasses import dataclass, field

from Fleet import Fleet


@dataclass
class Tile:
    __hit: False = field(default_factory=bool)
    contains: None = field(default_factory=Fleet)

    @property
    def hit(self):
        return self.__hit

    @hit.setter
    def hit(self, value: bool):
        self.__hit = value

    @property
    def has(self):
        return self.contains
