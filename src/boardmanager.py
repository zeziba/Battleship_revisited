import shipmanager

WATERSYMBOL = '~'


class BoardManager():
    def __init__(self, config, player):
        self.config = config
        self.player = player
        # TODO: Check if player or other is asking for information and morph output based on it

        self.__board = {
            "display": list(),
            "ships": list(),
            'point map': list()
        }

    @property
    def board(self):
        return self.__board

    @property
    def point_map(self):
        return self.board['point map']

    @property
    def ships(self):
        return self.board['ships']

    @property
    def display(self):
        return self.board['display']

    @property
    def size(self):
        return int(self.config['board size'])

    def add_ship(self, ship: type(shipmanager.ShipManager)):
        self.__board['ships'].append(ship)

    def __iter__(self):
        # The below should output the display board
        for row in self.board["display"]:
            yield row

    def reset(self):
        self.__board = {
            "display": list(),
            "ships": list(),
            'point map': list()
        }

    def update_display(self):
        self.__board['display'] = [WATERSYMBOL * self.config['board size'] for _ in range(self.config['board size'])]
        for ship in self.board['ships']:
            symbol = "X" if not ship.sunk else ship.symbol if ship.sunk else WATERSYMBOL
            for hit in ship.hits:
                t = list(self.__board['display'][hit[0]])
                t[1] = symbol
                self.__board['display'][hit[0]] = "".join(t)

    def update_point_map(self):
        self.update_display()
        self.__board['point map'] = list()
        for row in self.board['display']:
            self.__board['point map'].append([0 if x is not WATERSYMBOL else 1 for x in row])
            # TODO: Add ships that are sunk to the board
