from dataclasses import dataclass, field


@dataclass
class Tile:
    __contains: None
    __hit: False = field(default=bool)

    @property
    def hit(self) -> bool:
        return self.__hit

    @hit.setter
    def hit(self, value: bool) -> None:
        if not self.hit:
            self.__hit = value

    @property
    def contains(self):
        return self.__contains is not None

    @contains.setter
    def contains(self, value):
        if self.contains is True:
            raise IndexError(f"Location already has {self.contains}")
        self.__contains = value

    @property
    def has(self) -> object:
        return self.__contains
