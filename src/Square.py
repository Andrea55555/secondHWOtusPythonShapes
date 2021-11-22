from src.Figure import Figure


class Square(Figure):
    area = 0
    perimeter = 0
    name = 'square'

    def __init__(self, a):
        if a < 0:
            raise AttributeError
        self.a = a

    @property
    def get_area(self):
        self.area = self.a * 2
        return self.area

    @property
    def get_perimeter(self):
        self.perimeter = self.a * 4
        return self.perimeter

    def add_area(self, figure):
        self.area = self.area + figure.get_area()
        return self.area

