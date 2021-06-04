from dataclasses import dataclass, field

import Board as Board
import Fleet as Fleet
import GameRules as GameRules
import Player as Player
import Ship
import UI as UI

TESTING = False


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
        self.__set_up()
        self.UI = UI.UI()

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

    def __set_up(self) -> None:
        for index, i in enumerate(self.players):
            state = Player.State.AI if i is False else Player.State.PERSON
            self.__players[f"p{index}"] = Player.Player(
                state, Board.Board(), Fleet.GeneralFleet()
            )

    def set_up(self) -> None:
        self.__set_up()
        for p in self.player:
            i = 0
            p.board.generate_board()
            p.fleet.generate()
            if TESTING:
                for ship in p.get_ships:
                    ship.place_ship(i := i + 1, 0, p.board)
            else:
                if p.state is Player.State.AI:
                    for ship in p.get_ships:
                        ship.place_ship(i := i + 1, 0, p.board)
                else:
                    ships = [ship for ship in p.get_ships]
                    while ships:
                        ship = ships.pop()
                        print(GameRules.OUTPUTS[3].format(ship.name))
                        x, y = self.UI.get_selection(GameRules.OUTPUTS[0]).split(" ")
                        x = int(x)
                        y = int(y)
                        h_v = self.UI.get_selection(GameRules.OUTPUTS[1])
                        if (
                            not GameRules.check_xy(x, y)
                            or h_v not in "hv"
                            or any(
                                s.contains(px, py)
                                for s in p.get_ships
                                for px, py in Ship.Ship.possible_places(
                                    x, y, s.length, s.directionality
                                )
                            )
                        ):
                            print(GameRules.OUTPUTS[4].format(ship.name, x, y, h_v))
                            ships.append(ship)
                            continue
                        ship.directionality = (
                            Ship.Direction.HORIZONTAL
                            if h_v == "h"
                            else Ship.Direction.VERTICAL
                        )
                        ship.place_ship(x, y, p.board)
        self.start()

    def check_win(self) -> bool:
        for p in self.player:
            if p.destroyed:
                self.stop()
                return True
        return False


if __name__ == "__main__":
    game = Game((False, True))
    game.set_up()
