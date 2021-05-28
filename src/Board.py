from dataclasses import dataclass, field

import Tile

SIZE: int = 10


@dataclass()
class Board:
    __tiles: list[Tile.Tile] = field(
        init=False, default_factory=list[Tile.Tile]
    )

    @property
    def tiles(self) -> tuple[Tile.Tile]:
        return tuple(self.__tiles)

    def get(self, px, py):
        return self.tiles[px + py * SIZE]

    def tiles_set(self, x:int, y: int, tile: Tile) -> None:
        self.__tiles[x + y * SIZE] = tile

    def generate_board(self):
        self.__tiles = [Tile.Tile(False, None) for _ in range(SIZE * SIZE)]
