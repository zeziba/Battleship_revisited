import src.Player as Player
import src.Board as Board
import src.Fleet as Fleet
import src.GameRules as GameRules
from dataclasses import dataclass, field


@dataclass()
class Game:
    """
    Create and maintain the differing objects to enable a game of battleship to be played.

    Objects:
        Player
        Board -> Tile
        Fleet -> Ship

    The rules of the game are "simple."
    """

    players: tuple[bool, bool]
    __players: dict = field(default_factory=dict)
    state: GameRules.State = field(default=GameRules.State.STOPPED)

    def __post_init__(self):
        for index, i in enumerate(self.players):
            state = Player.State.AI if i is False else Player.State.PERSON
            self.__players[f"p{index}"] = Player.Player(
                state, Board.Board(), Fleet.GeneralFleet()
            )

    @property
    def player(self):
        for p in self.__players:
            yield self.__players[p]

    def stop(self) -> None:
        self.state = GameRules.State.STOPPED

    def start(self) -> None:
        self.state = GameRules.State.RUNNING

    @property
    def stopped(self) -> bool:
        return self.state == GameRules.State.STOPPED

    def set_up(self) -> None:
        for p in self.player:
            i = 0
            p.board.generate_board()
            p.fleet.generate()
            # Testing only
            for ship in p.get_ships:
                ship.place_ship(i := i + 1, 0, p.board)
        self.start()

    def check_win(self) -> bool:
        for p in self.player:
            if p.destroyed:
                self.stop()
                return True
        return False


if __name__ == "__main__":
    game = Game((False, False))
