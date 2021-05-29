import src.Player as Player
import src.Board as Board
import src.Fleet as Fleet
import src.GameRules as GameRules

class Game:
    """
    Create and maintain the differing objects to enable a game of battleship to be played.

    Objects:
        Player
        Board -> Tile
        Fleet -> Ship

    The rules of the game are simple.
    """
    def __init__(self, players: tuple[bool] = (False, False)) -> None:
        self.state = GameRules.State.STOPPED
        self.players = dict()
        for index, i in enumerate(players):
            state = Player.State.AI if i is False else Player.State.PERSON
            self.players[f"p{index}"] = Player.Player(state, Board.Board(), Fleet.GeneralFleet())
        print("\n".join([str(p) for p in self.players]))

    @property
    def game(self) -> Player.Player:
        while self.state is GameRules.State.RUNNING:
            for player in self.players:
                yield self.players[player]
                if self.players[player].destroyed:
                    self.state = GameRules.State.STOPPED


if __name__ == "__main__":
    game = Game()
