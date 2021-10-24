from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


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


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def get_area(self):
        return self.a * self.b

    @property
    def get_perimeter(self):
        return (self.a + self.b) * 2


Rectangle1 = Rectangle(12, 13)

print(Rectangle1.get_area)
print(Rectangle1.get_perimeter)


class Square(Figure):

    def __init__(self, a):
        self.a = a

    @property
    def get_area(self):
        return self.a * 2

    @property
    def get_perimeter(self):
        return self.a * 4


Square1 = Square(12)

print(Square1.get_area)
print(Square1.get_perimeter)
