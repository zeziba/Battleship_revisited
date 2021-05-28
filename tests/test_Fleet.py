import pytest

import src.Fleet


def test_fleet():
    for item in list(src.Fleet.Fleet):
        assert item.name is not None
        assert item.value is not None


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

    def test_place_fleet(self):
        fleet = src.Fleet.GeneralFleet()
        assert fleet.place_fleet() is None
        # TODO: Finish out this test

    def test_generated_fleet(self, resource):
        """Tests Generated Fleet"""
        f = resource
        assert f.fleet is not None
        for ship in f.fleet:
            assert type(f.fleet[ship]) is src.Fleet.Ship
