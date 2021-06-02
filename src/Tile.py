from dataclasses import dataclass, field


@dataclass
class Tile:
    __contains: None
    __hit: False = field(default_factory=bool)

    @property
    def hit(self) -> bool:
        return self.__hit

    @hit.setter
    def hit(self, value: bool) -> None:
        if not self.hit:
            self.__hit = value

    @property
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        if self.contains is not None:
            raise IndexError(f"Location already has {self.contains}")
        self.__contains = value

    @property
    def has(self) -> object:
        return self.contains
