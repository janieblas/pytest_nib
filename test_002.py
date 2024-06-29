"""
Filename: test_002.py
Description: This file contains tests for the 'increment_function' function 
             that increments a value by 1.

Author: janieblas
Date Created: 29/06/2024
Last Modified: 29/06/2024
"""
import pytest

# Definir una función de prueba parametrizada usando el decorador pytest.mark.parametrize
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (5, 6),
    (10, 11),
    (-1, 0),
])
def test_increment_function(input, expected):
    result = increment_function(input)
    assert result == expected

def increment_function(x):
    return x + 1