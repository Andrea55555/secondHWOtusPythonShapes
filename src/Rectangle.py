from src.Figure import Figure


class Rectangle(Figure):
    area = 0
    perimeter = 0
    name = 'rectangle'

    def __init__(self, a, b):
        if a < 0:
            raise AttributeError
        if b < 0:
            raise AttributeError
        self.a = a
        self.b = b


    @property
    def get_area(self):
        self.area = self.a * self.b
        return self.area

    @property
    def get_perimeter(self):
        self.perimeter = (self.a + self.b) * 2
        return self.perimeter

    def add_area(self, figure):
        self.area = self.area + figure.get_area()
        return self.area
