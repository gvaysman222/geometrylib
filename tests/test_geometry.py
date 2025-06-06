import math
import pytest
from geometry.circle import Circle
from geometry.triangle import Triangle
from geometry.calculate import calculate_area

def test_circle_area():
    circle = Circle(1)
    assert math.isclose(circle.get_area(), math.pi, rel_tol=1e-6)

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert math.isclose(triangle.get_area(), 6.0, rel_tol=1e-6)

def test_triangle_right_angled():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_angled()

def test_calculate_area_polymorphic():
    shape = Circle(2)
    area = calculate_area(shape)
    assert math.isclose(area, math.pi * 4, rel_tol=1e-6)

def test_invalid_circle():
    with pytest.raises(ValueError):
        Circle(0)

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)
