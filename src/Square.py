from src.Figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.a = a

    @property
    def get_area(self):
        return self.a * 2

    @property
    def get_perimeter(self):
        return self.a * 4

    @property
    def add_area_other_figures(self):
        pass


Square1 = Square(12)

print(Square1.get_area)
print(Square1.get_perimeter)
