import shipmanager

DIRS = {
    'VERTICAL': (1, 0),
    'HORIZONTAL': (0, 1)
}

DIFFICULTY = {
    0: "easy",
    1: "medium",
    3: "hard"
}


class Player:
    def __init__(self, _type, board, config, name="Player"):
        self.__type = _type
        self.__board = board
        self.__config = config
        self.__ships = {i.split(":")[0]: int(i.split(":")[1]) for i in self.__config['ships'].split(',')}
        self.__turn = 0
        self.name = name

    def place_boats(self, _dir, boat, x, y):
        if _dir not in DIRS:
            raise Exception("Direction is not a direction")
        if boat not in self.__ships.keys():
            raise Exception("Direction is not a direction")
        self.__board[boat] = shipmanager.ShipManager(self.__config, boat, boat[0])
        self.__board[boat].create_ship(_dir, x, y)

    def fire_shot(self, **kwargs):
        """
        :param kwargs:
            :kwargs board: boardmanager.BoardManager
            :kwargs x: Int x position
            :kwargs y: Int y position
        :return: True/False if shot hit
        """
        # This method will be used by the opponent
        self.__turn += 1
        for ship in kwargs['board'].ships:
            if ship.hit(kwargs['x'], kwargs['y']):
                return True
        return False

    @property
    def ship_names(self):
        for boat in self.__ships.keys():
            yield boat

    @property
    def turn(self):
        return self.__turn


class AI(Player):
    def __init__(self, board, config, difficulty):
        super().__init__('computer', board, config)
        import datetime
        self.name = "AI: {}".format(hash(datetime.datetime.now()))

        self.__difficulty = difficulty

    def fire_shot(self, **kwargs):
        opp = kwargs['board']
        opp.update_point_map()
        # Need to generate a list of possible solutions to the above board based on the difficulty of the situation
        if self.__difficulty == 'easy':
            return self.__easy_ai__(opp)
        elif self.__difficulty == 'medium':
            pass
        elif self.__difficulty == 'hard':
            pass

    @staticmethod
    def _get_adjacent_cells(x, y, board):
        left    = board.point_map[x - 1][y] if x - 1 > 0 else 0
        top     = board.point_map[x][y - 1] if y - 1 > 0 else 0
        bottom  = board.point_map[x][y + 1] if y + 1 < board.size else 0
        right   = board.point_map[x + 1][y] if x + 1 < board.size else 0
        return left + right + top + bottom

    def __easy_ai__(self, board):
        board.update_display()
        # Get the point map by adding the adjacent squares values together, this should return a min of 1 if
        #   the map has a water spot under the square and ALWAYS 0 if there is a hit at that location
        point_map = [self._get_adjacent_cells(x, y, board) for x in range(board.size) for y in range(board.size)]
        # Simple conversion: (x, y) -> x = num % board.size, y = num / size
        max = 0
        _max = -1
        for index, pos in enumerate(point_map):
            if point_map[index] > _max:
                _max = index
                max = pos
            if board.point_map[pos % board.size][pos // board.size] == 0:
                point_map[pos % board.size][pos // board.size] = 0
        import random
        possible_moves = [(index % board.size, index // board.size) for index, pos in enumerate(point_map)
                          if point_map[index] == max]
        return random.choice(possible_moves)


