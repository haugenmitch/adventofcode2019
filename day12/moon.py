import operator

class Moon:

    def __init__(self, x, y, z):
        self.__pos = (x, y, z)
        self.__vel = (0, 0, 0)
        self.__update = (0, 0, 0)

    def pos(self):
        return self.__pos

    def energy(self):
        pe = abs(self.__pos[0]) + abs(self.__pos[1]) + abs(self.__pos[2])
        ke = abs(self.__vel[0]) + abs(self.__vel[1]) + abs(self.__vel[2])
        return pe * ke

    def compare(self, other_pos):
        x = (1 if other_pos[0] > self.__pos[0] else -1 if other_pos[0] < self.__pos[0] else 0) + self.__update[0]
        y = (1 if other_pos[1] > self.__pos[1] else -1 if other_pos[1] < self.__pos[1] else 0) + self.__update[1]
        z = (1 if other_pos[2] > self.__pos[2] else -1 if other_pos[2] < self.__pos[2] else 0) + self.__update[2]
        self.__update = (x, y, z)

    def update_velocity(self):
        self.__vel = tuple(map(operator.add, self.__vel, self.__update))
        self.__update = (0, 0, 0)

    def move(self):
        self.__pos = tuple(map(operator.add, self.__pos, self.__vel))