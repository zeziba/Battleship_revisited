import pytest
import src.Board as Board


@pytest.fixture
def empty_tile():
    return Board.TileType.EMPTY


def empty_board(count):
    """Returns a Board obj with each tile empty"""
    for _ in range(count):
        yield Board.Board(tuple(Board.TileType.EMPTY for _ in range(count)))


def test_tile_type():
    for index, item in enumerate(Board.TileType):
        assert (index + 1) is item.value
        assert item.name is not None


@pytest.mark.parametrize("data", empty_board(Board.SIZE // 10))
def test_board(data):
    assert type(data) is Board.Board
    assert all(data.board[i] is Board.TileType.EMPTY for i in range(len(data.board)))
