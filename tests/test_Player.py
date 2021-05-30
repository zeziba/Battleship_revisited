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
        assert hasattr(player, "generate_fleet")

    def test_player_has_get_ships(self, player):
        assert hasattr(player, "get_ships")

    def test_player_get_ships(self, player):
        p = player
        p.generate_fleet()
        b = src.Player.Board.Board()
        b.generate_board()
        for index, ship in enumerate(p.fleet.fleet):
            p.fleet.fleet[ship].place_ship(index, 0, b)
        for ship in p.get_ships:
            assert type(ship) is src.Player.Fleet.Ship.Ship

    @pytest.mark.parametrize("nth", [0 for _ in range(10)])
    def test_player_fleet_placement(self, player, nth):
        # TODO: Finish implementing
        p = player
        assert len(p.fleet.fleet) == 0
        p.generate_fleet()
        assert len(p.fleet.fleet) > 0

    def test_player_destroyed(self, player):
        p = player
        assert p.destroyed is True
        p.fleet.generate()
        assert p.destroyed is False
        for ship in p.fleet.fleet:
            p.fleet.fleet[ship].hit_points = 0
        assert p.destroyed is True
