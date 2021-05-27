import pytest
import src.Player as Player
from random import choice
import src.Board as Board


# Number of times to run the test
N = 10


def test_player_type():
    player = choice(list(Player.PlayerType))
    return Player.Player(player, Board.Board(tuple(Board.TileType.EMPTY for _ in range(100))))


@pytest.mark.parametrize("ind", range(N))
def test_player(ind):
    player = test_player_type()
    assert type(player) is Player.Player
    assert player.type.value >= 0
