import boardmanager
import configmanager
import gamemanager
import playermanager
import uxhandler


class Battleship():
    def __init__(self):
        config = configmanager.ConfigManager()
        try:
            config.open()
        except FileNotFoundError:
            config.create()
        self.config = config.get_config()['settings']
        self.ux = uxhandler.UXHandle(self.config)
        self.game = gamemanager.GameManager(self.config)

    def start(self):
        # Start the game
        # Ask the player for their name, if empty assume they want to have robots play one another
        name = self.ux.get_input(self.ux.out["get name"])

        player_board = boardmanager.BoardManager(self.config, name) \
            if name else boardmanager.BoardManager(self.config, "AI")
        player = playermanager.Player(name, player_board, self.config) \
            if name else playermanager.AI(player_board, self.config, playermanager.DIFFICULTY[0])

        ai_board = boardmanager.BoardManager(self.config, "AI")
        ai = playermanager.AI(ai_board, self.config, playermanager.DIFFICULTY[0])

        self.game.game(player1=player, player2=ai, player1_board=player_board, player2_board=ai_board, ux=self.ux)


if __name__ == "__main__":
    b = Battleship()
    b.start()
