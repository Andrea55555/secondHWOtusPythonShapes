from src.Figure import Figure


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
