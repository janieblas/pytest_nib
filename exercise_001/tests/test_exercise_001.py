# exercise_001.py

import pytest
import sys
sys.path.append('C:\\Embedded_SMT32\\pytest_studying\\exercise_001')  # Ajusta la ruta según tu estructura

from exercise_001 import calcular_area_rectangulo

# Caso de prueba 1: Base y altura positivas
def test_area_rectangulo_base_positiva_altura_positiva():
    assert calcular_area_rectangulo(3, 4) == 12

# Caso de prueba 2: Base negativa, debe lanzar ValueError
def test_area_rectangulo_base_negativa():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-1, 5)

# Caso de prueba 3: Altura cero, debe lanzar ValueError
def test_area_rectangulo_altura_cero():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(2, 0)

# Caso de prueba 4: Base y altura cero, debe lanzar ValueError
def test_area_rectangulo_base_cero_altura_cero():
    with pytest.raises(ValueError):
        calcular_area_rectangulo(0, 0)

# Caso de prueba 5: Números decimales
def test_area_rectangulo_numeros_decimales():
    assert calcular_area_rectangulo(2.5, 3) == 7.5

# Ejecución del cálculo directo
print(calcular_area_rectangulo(5, 3))
