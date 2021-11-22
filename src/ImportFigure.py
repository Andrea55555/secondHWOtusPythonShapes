from src.Ciacle import Ciacle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

ciacle1 = Ciacle(12)
triangle1 = Triangle(12, 13, 14)
square1 = Square(12)
rectangle1 = Rectangle(12, 13)

figures = [ciacle1, triangle1, square1, rectangle1]
for item in figures:
    print(item, ' area= ', item.get_area)
