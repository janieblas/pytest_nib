import pytest
import sys
sys.path.append('C:\\Embedded_SMT32\\pytest_studying\\exercise_002')

from exercise_002 import calculate_triangle_area

def test_area_triangulo_base_positiva_altura_positiva():
    assert calculate_triangle_area(3,4) == 6

def test_area_triangulo_base_negativa_altura_positiva():
    with pytest.raises(ValueError):
        calculate_triangle_area(-3,4)

def test_area_triangulo_base_cero_altura_cero():
    with pytest.raises(ValueError):
        calculate_triangle_area(0, 0)
