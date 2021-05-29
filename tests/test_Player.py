import pytest
import src.Player
from random import choice


def test_enum_state():
    for i in src.Player.State:
        assert hasattr(i, "name")
        assert hasattr(i, "value")


@pytest.fixture()
def player():
    return src.Player.Player(
        choice(list(src.Player.State)),
        src.Player.Board.Board(),
        src.Player.Fleet.GeneralFleet(),
    )


class TestPlayer:
    def test_player_setup(self, player):
        assert player is not None

    def test_player_has_state(self, player):
        assert hasattr(player, "state")

    def test_player_has_fleet(self, player):
        assert hasattr(player, "fleet")

    def test_player_has_board(self, player):
        assert hasattr(player, "board")

    def test_player_can_place_fleet(self, player):
        assert hasattr(player, "place_fleet")

    @pytest.mark.parametrize("nth", [0 for _ in range(10)])
    def test_player_fleet_placement(self, player, nth):
        p = player
        assert len(p.fleet.fleet) == 0
        p.place_fleet()
        assert len(p.fleet.fleet) > 0

    def test_player_destroyed(self, player):
        p = player
        assert p.destroyed is True
        p.fleet.generate()
        assert p.destroyed is False
        for ship in p.fleet.fleet:
            p.fleet.fleet[ship].hit_points = 0
        assert p.destroyed is True
