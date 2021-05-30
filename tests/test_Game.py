import pytest
import src.Game

src.Game.TESTING = True


@pytest.fixture()
def game():
    players = (False, False)
    yield src.Game.Game(players=players)


def get_coord():
    size = src.Game.GameRules.SIZE
    for i in range(size ** 2):
        yield i % size, i // size


class TestGame:
    def test_game_setup(self, game):
        assert game is not None

    def test_game_has_players(self, game):
        assert hasattr(game, "players")

    def test_game_has_player(self, game):
        assert hasattr(game, "player")

    def test_game_has_state(self, game):
        assert hasattr(game, "state")

    def test_game_has_stopped(self, game):
        assert hasattr(game, "stopped")

    def test_game_start(self, game):
        g = game
        assert g.stopped
        g.start()
        assert not g.stopped

    def test_game_stop(self, game):
        g = game
        assert g.stopped
        g.start()
        g.stop()
        assert g.stopped

    def test_game_players(self, game):
        assert type(game.players) is tuple
        for i in game.players:
            assert type(i) is bool

    def test_game_dict_players(self, game):
        assert all(type(p) is src.Game.Player.Player for p in game.player)

    def test_game_set_up(self, game):
        g = game
        for p in g.player:
            assert len(p.fleet.fleet) == 0
            assert len(p.board.tiles) == 0
        g.set_up()
        for p in g.player:
            assert len(p.fleet.fleet) == len(src.Game.GameRules.FLEET)
            assert len(p.board.tiles) == src.Game.GameRules.SIZE ** 2

    def test_game_check_win(self, game):
        g = game
        assert g.stopped
        g.set_up()
        size = src.Game.GameRules.SIZE
        for i in range(size ** 2 - 1):
            x, y = i % size, i // size
            for p in g.player:
                assert not g.stopped
                p.fleet.hit(x, y)
            if g.check_win():
                break
        assert g.stopped

    def test_game_game(self, game):
        pass
