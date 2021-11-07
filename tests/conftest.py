import pytest

from src.Ciacle import Ciacle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture
def default_ciacle():
    ciacle = Ciacle(12)
    yield ciacle
    del ciacle


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(12, 13)
    yield rectangle
    del rectangle


@pytest.fixture
def default_square():
    square = Square(12)
    yield square
    del square


@pytest.fixture
def default_triangle():
    triangle = Triangle(12, 13, 14)
    yield triangle
    del triangle
