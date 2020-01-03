class Moon2:

    def __init__(self, x):
        self.__pos = x
        self.__vel = 0
        self.__update = 0

    def pos(self):
        return self.__pos

    def vel(self):
        return self.__vel

    def energy(self):
        return abs(self.__pos) * abs(self.__vel)

    def compare(self, other_pos):
        self.__update = (1 if other_pos > self.__pos else -1 if other_pos < self.__pos else 0) + self.__update

    def update_velocity(self):
        self.__vel += self.__update
        self.__update = 0

    def move(self):
        self.__pos += self.__vel

    def __eq__(self, other):
        if not isinstance(other, Moon2):
            return NotImplemented

        return self.pos() == other.pos() and self.vel() == other.vel()
