# test_001.py
"""
Filename: test_001.py
Description: This file contains tests for the 'sample_data' function 
             that contains a dictionary.

Author: janieblas
Date Created: 29/06/2024
Last Modified: 29/06/2024
"""
import pytest

@pytest.fixture
def sample_data():
    # Setup code: Create some sample data
    data = {"name": "Alice", "age": 30}
    yield data
    # Teardown code: Clean up if necessary
    data.clear()
    print("Teardown complete")

def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30

def test_sample_data_modification(sample_data):
    sample_data["age"] += 1
    assert sample_data["age"] == 31