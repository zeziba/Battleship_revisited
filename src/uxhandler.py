import os
import boardmanager

FILENAME = "output.txt"


class UXHandle:
    def __init__(self, config):
        self.config = config
        self.out = dict()
        self.load()

    def load(self):
        filename = os.path.join(self.config["base location"], FILENAME)
        with open(filename, "r") as file:
            for line in file:
                data = line.split(":")
                self.out[data[0]] = data[1]

    def get(self, option):
        return self.config[option]

    @staticmethod
    def print_board(board):
        if not isinstance(board, boardmanager.BoardManager):
            raise TypeError()

        for row in board:
            print(os.path.join("{}" * int(board.config["board size"])).format(*row))
