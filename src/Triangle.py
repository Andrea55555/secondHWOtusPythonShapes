import math
from src.Figure import Figure


class Triangle(Figure):
    area = 0
    perimeter = 0
    name = 'triangle'

    def __init__(self, a, b, c):
        if a < 0:
            raise AttributeError
        if b < 0:
            raise AttributeError
        if c < 0:
            raise AttributeError
        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        self.area = math.sqrt((p * (p - self.a) * (p - self.b) * (p - self.c)))
        return self.area

    @property
    def get_perimeter(self):
        self.perimeter = self.a + self.b + self.c
        return self.perimeter

    def add_area(self, figure):
        self.area = self.area + figure.get_area()
        return self.area

