import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def distance(self, x, y):
        distance = abs(x - self.x)**2 + abs(y - self.y)**2

        return math.sqrt(distance)
