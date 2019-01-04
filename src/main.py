import configmanager
import uxhandler
import boardmanager
import gamemanager


class Battleship():
    def __init__(self):
        config = configmanager.ConfigManager()
        self.config = config.get_config()
        self.ux = uxhandler.UXHandle(self.config)
        self.board = boardmanager.BoardManager(self.config)
        self.game = gamemanager.GameManager(self.config)

    def start(self):
        pass
