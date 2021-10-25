from src.Ciacle import Ciacle
from src.Figure import Figure
import math


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def get_area(self):
        p = (self.a + self.b + self.c) / 2  # если имеем 3 переменные то считаем в противном случае вывести none
        return math.sqrt((p * (p - self.a) * (p - self.b) * (p - self.c)))

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c

    @property
    def add_area(self, ciacle1):
        ciacle1 = Ciacle(5)
        return self.get_area(Triangle1) + ciacle1  # научить складывать с другой геометрической фигурой
        # и Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError)


Triangle1 = Triangle(12, 13, 14)
