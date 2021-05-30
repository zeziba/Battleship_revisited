import pytest

import src.Board


@pytest.fixture()
def board():
    yield src.Board.Board()


class TestBoard:
    def test_board_setup(self, board):
        assert board is not None

    def test_board_has_tiles(self, board):
        assert hasattr(board, "tiles") is True

    def test_board_has_tiles_setter(self, board):
        assert hasattr(getattr(type(board), "tiles", None), "fset")

    def test_board_tiles_setter(self, board):
        b = board
        b.generate_board()
        assert b.get(0, 0).has is None
        b.tiles_set(0, 0, src.Board.Tile.Tile(False, "Ship"))

    def test_board_get(self, board):
        b = board
        b.generate_board()
        for index, _ in enumerate(b.tiles):
            # px + py * SIZE
            x, y = index % src.Board.SIZE, index // src.Board.SIZE
            assert b.get(x, y) is not None

    def test_board_generate_board(self, board):
        b = board
        assert len(b.tiles) == 0
        b.generate_board()
        assert len(b.tiles) == src.Board.SIZE ** 2
        for t in b.tiles:
            assert type(t) is src.Board.Tile.Tile
