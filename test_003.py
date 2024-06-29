"""
Filename: test_002.py
Description: This file contains tests for differents asserts.

Author: janieblas
Date Created: 29/06/2024
Last Modified: 29/06/2024
"""

import pytest

# Afirmación básica
def test_addition():
    assert 1 + 1 == 2

# Afirmación con mensaje personalizado
def test_multiplication():
    result = 2 * 3
    assert result == 6, f"Expected multiplication result to be 6, but got {result}"

# Afirmación con assert expr, msg
def test_division():
    numerator = 10
    denominator = 2
    assert denominator != 0, "Denominator should not be zero"
    assert numerator / denominator == 5, f"Expected division result to be 5, but got {numerator / denominator}"

# Afirmación con assert expr1 == expr2
def test_string_concatenation():
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    assert full_name == "John Doe"

# Afirmación con assert expr1 in expr2
def test_list_contains():
    numbers = [1, 2, 3, 4, 5]
    assert 3 in numbers

# Afirmación con assert expr1 is expr2
def test_object_identity():
    a = [1, 2, 3]
    b = a
    assert a is b
