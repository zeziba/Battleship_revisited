from random import choice

import pytest

import src.Tile


@pytest.fixture()
def tile():
    yield src.Tile.Tile(False, choice(list(src.Tile.Fleet)))


class TestTile:
    def test_tile_setup(self, tile):
        assert tile is not None

    def test_tile_has_hit(self, tile):
        assert hasattr(tile, "hit")

    def test_tile_has_contains(self, tile):
        assert hasattr(tile, "contains")

    def test_tile_init_hit(self, tile):
        assert tile.hit is False

    def test_tile_can_hit(self, tile):
        t = tile
        t.hit = not t.hit
        assert t.hit is True