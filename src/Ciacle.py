from src.Figure import Figure
import math


class Ciacle(Figure):

    def __init__(self, r):
        self.r = r

    @property
    def get_area(self):
        return math.pi * (self.r ** 2)

    @property
    def get_perimeter(self):
        return 2 * 3.14 * self.r


Ciacle1 = Ciacle(12)

print(Ciacle1.get_area)
print(Ciacle1.get_perimeter)