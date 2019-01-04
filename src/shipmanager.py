

class ShipManager():
    def __init__(self, config, name, symbol):
        self.config = config
        self.__symbol = symbol
        self.__name = name
        self._length = self.config[name]

        self.__hits = list()
        self.__positions = list()

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def hits(self):
        return self.__hits

    @property
    def position(self):
        return self.__positions

    @property
    def length(self):
        return self._length

    def reset(self):
        self.__positions = list()
        self.__hits = list()

    def create_ship(self, _dir, x0, y0):
        if not self.position:
            for i in range(self.length):
                self.__positions.append([x0 + 1 * _dir[0], y0 + 1 * _dir[1]])
            return True
        else:
            return False

    def hit(self, x, y):
        if [x, y] not in self.position:
            return False
        elif [x, y] in self.hits:
            raise Exception("Already Fired Here")
        self.__hits.append([x, y])
        return True

    def sunk(self):
        if set(set(self.position) - set(self.hits)):
            return False
        return True
