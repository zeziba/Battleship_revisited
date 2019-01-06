import boardmanager


class GameManager():
    def __init__(self, config):
        self.config = config

        self.__state = False

    @property
    def state(self):
        return self.__state

    def reset(self):
        self.__state = False

    def check_win(self, board, override=False):
        if not override:
            if not isinstance(board, boardmanager.BoardManager):
                raise TypeError("Not a board object")

        ship_count = int(self.config['ship count'])
        if len(board.board['ships']) > ship_count:
            raise Exception("Too many ships present on the board!")

        if not self.check_if_valid(board):
            raise Exception("Board is malformed")

        if all(boat.sunk for boat in board.board['ships']):
            self.__state = True
            return True
        return False

    @staticmethod
    def _m(ship1, ship2):
        if ship1[0] == ship2[0]:
            return float('inf')
        return (ship2[1] - ship1[1]) / (ship2[0] - ship1[0])

    def _check_if_in_bounds(self, ship):
        if ship[0] < 0 or ship[1] < 0 or ship[0] > self.config['board size'] or ship[1]:
            return False
        return True

    def _check_ship_is_valid(self, ship):
        m = self._m(ship.positions[0], ship.positions[1])

        x0, y0 = ship.positions[0][0], ship.positions[0][1]

        for pos in ship.positions:
            self._check_if_in_bounds(pos)
            n_m = self._m([x0, y0], pos)
            if m != n_m or n_m != float('inf') or n_m == 0:
                return False
            if pos[0] - x0 > ship.length or pos[1] - y0 > ship.length:
                return False
        if len(set([tuple(pos) for pos in ship.positions])) != ship.length:
            return False
        return True

    def check_if_valid(self, board):
        # Check if the board is valid, display board is not checked.
        # Does this by checking if the correct number of ships is present then checks the position of each.
        # Checks if a player has won the game and returns a value based on that information
        ships_available = {i.split(":")[0].lower().replace('"', ""): int(i.split(":")[1]) for i in self.config['ships'].split(',')}
        ship_data = {ship.name: 0 for ship in board.ships}

        # Check if ships are inside the board along with number of each type
        for ship in board.ships:
            ship_data[ship.name] += 1

        for ship in board.ships:
            if int(ship_data[ship.name]) != int(ships_available[ship.name]):
                return False

            if not self._check_ship_is_valid(ship):
                return False

        return True
