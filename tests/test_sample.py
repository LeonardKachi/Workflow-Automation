"""
Sample tests for the project
"""
import pytest
import random

def test_addition():
    """Test basic arithmetic"""
    assert 1 + 1 == 2

def test_list_operations():
    """Test list manipulation"""
    items = [1, 2, 3]
    items.append(4)
    assert len(items) == 4
    assert items[-1] == 4

def test_random_generation():
    """Test random number generation within bounds"""
    value = random.randint(1, 100)
    assert 1 <= value <= 100

def test_string_operations():
    """Test string methods"""
    text = "Hello, World!"
    assert text.startswith("Hello")
    assert text.endswith("!")
    assert "World" in text

class TestMathOperations:
    """Test class for math operations"""
    
    def test_multiplication(self):
        assert 3 * 4 == 12
    
    def test_division(self):
        assert 10 / 2 == 5
    
    def test_power(self):
        assert 2 ** 3 == 8
