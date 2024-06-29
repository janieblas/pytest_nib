# pytest_000.py

"""
Filename: test_000.py
Description: This file contains tests for the 'inc' function 
             that increments a value by 1.

Author: janieblas
Date Created: 29/06/2024
Last Modified: 29/06/2024
"""

def inc(x):
    """
    Function that increments the value of x by 1.
    
    Parameters:
    x (int): Value to increment.
    
    Returns:
    int: Value incremented by 1.
    """
    return x + 1

def test_answer():
    """
    Test Case ID: TC001
    Description: Verifies that the 'inc' function increments the value correctly.
    Expected Result: 4 when the input is 3.
    """
    assert inc(3) == 4  # This assertion should pass for the test to be successful

def test_negative():
    """
    Test Case ID: TC002
    Description: Verifies that the 'inc' function handles negative numbers correctly.
    Expected Result: -2 when the input is -3.
    """
    assert inc(-3) == -2
