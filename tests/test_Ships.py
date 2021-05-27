import pytest
from random import choice
import src.Ships as Ship

# Number of times to run the test
N = 10


def test_ship():
    ship = choice(list(Ship.ShipType))
    return Ship.Ship(ship, Ship.Lengths[ship], list(_ for _ in range(Ship.Lengths[ship])))


@pytest.mark.parametrize("ind", range(N))
def test_ship_type(ind):
    tship = test_ship()
    assert type(tship) is Ship.Ship
    assert tship.length == Ship.Lengths[tship.type]
    assert len(tship.positions) == Ship.Lengths[tship.type]
