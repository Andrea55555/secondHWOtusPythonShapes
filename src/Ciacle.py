import math

from src.Figure import Figure


class Ciacle(Figure):
    name = 'ciacle'
    area = 0
    perimeter = 0

    def __init__(self, r):
        self.r = r

    @property
    def get_area(self):
        self.area = math.pi * (self.r ** 2)
        return self.area

    @property
    def get_perimeter(self):
        self.perimeter = 2 * 3.14 * self.r
        return self.perimeter

    def add_area(self, figure):
        self.area = self.area + figure.get_area()
        return self.area


