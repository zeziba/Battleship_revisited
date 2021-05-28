from random import choice, randint

import pytest

import src.Ship


def direction() -> src.Ship.Direction:
    return choice(list(src.Ship.Direction))


def ship() -> src.Ship.Ship:
    name = "".join([chr(randint(97, 122)) for _ in range(randint(10, 100))])
    length = randint(1, 5)
    return src.Ship.Ship(name, length, direction())


def test_direction():
    for d in src.Ship.Direction:
        assert type(d) is src.Ship.Direction
        assert d.name is not None
        assert d.value >= 0


@pytest.fixture()
def resource() -> src.Ship.Ship:
    yield ship()


def coord() -> int:
    return randint(0, 10)


class TestShip:
    def test_ship_setup(self, resource):
        assert resource is not None

    def test_ship_has_length(self, resource):
        assert hasattr(resource, "length")

    def test_ship_has_name(self, resource):
        assert hasattr(resource, "name")

    def test_ship_has_directionality(self, resource):
        assert hasattr(resource, "directionality")

    def test_ship_has_is_sunk(self, resource):
        assert hasattr(resource, "is_sunk")

    def test_ship_generation(self, resource):
        """Tests ship generation"""
        assert type(resource) is src.Ship.Ship
        assert resource.name is not None
        assert resource.length >= 0
        assert resource.hit_points >= 0
        assert resource.directionality is not None

    def test_ship_placement(self, resource):
        """Tests Ship Placement"""
        s = resource
        assert callable(s.place_ship)
        assert s.place_ship(coord(), coord()) is True
        assert s.place_ship(coord(), coord()) is False
        assert len(s.positions) == resource.length

    def test_ship_hit(self, resource):
        """Test if a ship is hit or not"""
        s = resource
        assert callable(s.hit)
        assert s.hit(coord(), coord()) is False
        s.place_ship(coord(), coord())
        start_hp = s.hit_points
        assert s.is_sunk is False
        for key in s.positions:
            y, x = key.split(",")
            assert start_hp == s.hit_points
            assert s.hit(int(x), int(y)) is True
            start_hp -= 1
            assert s.hit(int(x), int(y)) is False
            assert start_hp == s.hit_points
        assert s.is_sunk is True
