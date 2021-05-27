import Ships
import Player
import Board
import Game
import UImanager


def main():
    board = Board.Board(*(Board.TileType.EMPTY for _ in range(0, 100)))


if __name__ == "__main__":
    main()
