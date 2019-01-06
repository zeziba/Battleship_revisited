import configmanager
import uxhandler
import boardmanager
import gamemanager


class Battleship():
    def __init__(self):
        config = configmanager.ConfigManager()
        config.create()
        self.config = config.get_config()['settings']
        self.ux = uxhandler.UXHandle(self.config)
        self.board = boardmanager.BoardManager(self.config, None)
        self.game = gamemanager.GameManager(self.config)

    def start(self):
        pass


if __name__ == "__main__":
    b = Battleship()
