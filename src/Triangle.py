from src.Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt((p * (p - self.a) * (p - self.b) * (p - self.c)))

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c


Triangle1 = Triangle(12, 13, 14)

print(Triangle1.get_area)
print(Triangle1.get_perimeter)