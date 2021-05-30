import pytest

import src.Fleet


def test_fleet():
    for i in list(src.Fleet.Fleet):
        assert hasattr(i, "name")
        assert hasattr(i, "value")


def test_FLEET():
    for ship, value in src.Fleet.FLEET.items():
        assert ship in list(src.Fleet.Fleet)
        assert type(value) is int


@pytest.fixture()
def resource():
    f = src.Fleet.GeneralFleet()
    f.generate()
    yield f


class TestGenerateFleet:
    def test_fleet_setup(self, resource):
        assert resource is not None

    def test_fleet_has_fleet(self, resource):
        assert hasattr(resource, "fleet")

    def test_gen_fleet(self):
        """Tests Fleet Generation"""
        fleet = src.Fleet.GeneralFleet()
        assert len(fleet.fleet) == 0
        fleet.generate()
        assert len(fleet.fleet) == len(src.Fleet.FLEET)

    def test_generated_fleet(self, resource):
        """Tests Generated Fleet"""
        f = resource
        assert f.fleet is not None
        for ship in f.fleet:
            assert type(f.fleet[ship]) is src.Fleet.Ship.Ship

    def test_fleet_hit(self, resource):
        f = resource
        board = src.Fleet.Ship.Board.Board()
        board.generate_board()
        for ship in f.fleet:
            f.fleet[ship].place_ship(0, 0, board)
        for ship in f.fleet:
            for pos in f.fleet[ship].positions:
                y, x = pos.split(",")
                assert f.hit(x, y) is True
        assert f.hit(0, 0) is False
