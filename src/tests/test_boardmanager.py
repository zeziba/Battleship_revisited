import sys
import unittest

defaultconfig = {
    "base location": '',
    "config file": "config.ini",
    "board size": 10,
    "ship count": 5,
    "ships": '''"Battleship":1,"Carrier":1,"Patrol Boat":1,"Submarine":1,"Destroyer":1''',
    'Battleship': 4,
    'Carrier': 5,
    'Patrol Boat': 2,
    'Submarine': 3,
    'Destroyer': 3
}

test_point = [1, 1]


class testboat:
    def __init__(self, tp):
        self.tp = tp

    def hit(self, x, y):
        if x == self.tp[0] and y == self.tp[1]:
            return True
        return False


class testboard:
    def __init__(self, tb):
        self.__board = {
            "display": list(),
            "ships": list(),
            'point map': [[0 for _ in range(10)] for _ in range(10)]
        }
        self.__board['ships'].append(tb)

    @property
    def board(self):
        return self.__board

    @property
    def ships(self):
        return self.board['ships']

    @property
    def size(self):
        return defaultconfig['board size']

    @property
    def point_map(self):
        return self.__board['point map']


size = int(defaultconfig['board size'])


class TestMethodsBoardManager(unittest.TestCase):
    class MyOut(object):
        def __init__(self):
            self.data = []

        def write(self, s):
            self.data.append(s)

        def flush(self):
            self.data = []

        def getvalue(self):
            return self.data

        def __str__(self):
            return "".join(self.data)

    pass
