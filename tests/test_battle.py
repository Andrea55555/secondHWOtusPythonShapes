import pytest

from src.Ciacle import Ciacle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_negative_cicle(negative_ciacle):
    with pytest.raises(AttributeError):
        Ciacle(negative_ciacle)


def test_comparison_cicle(default_ciacle):
    assert default_ciacle.get_area == 452.3893421169302


def test_negative_triangle(negative_triangle):
    with pytest.raises(AttributeError):
        Triangle(negative_triangle.__getattribute__("first"), negative_triangle.__getattribute__("second"),
                 negative_triangle.__getattribute__("third"))


def test_comparison_triangle(default_triangle):
    assert default_triangle.get_area == 72.30793524918272


def test_negative_square(negative_square):
    with pytest.raises(AttributeError):
        Square(negative_square)


def test_comparison_square(default_square):
    assert default_square.get_area == 24


def test_negative_rectangle(negative_rectangle):
    with pytest.raises(AttributeError):
        Rectangle(negative_rectangle.__getattribute__("first"), negative_rectangle.__getattribute__("second"))


def test_comparison_rectangle(default_rectangle):
    assert default_rectangle.get_area == 156
