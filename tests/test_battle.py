import pytest

from src.Ciacle import Ciacle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_ciacle():
    with pytest.raises(AttributeError):
        Ciacle(12)


def test_rectangle():
    with pytest.raises(AttributeError):
        Rectangle(12, 13)


def test_square():
    with pytest.raises(AttributeError):
        Square(12)


def test_triangle():
    with pytest.raises(AttributeError):
        Triangle(12, 13, 14)