import pytest
from mylib2 import calculator


#--- Fixture Example---
@pytest.fixture(scope = "module")
def numbers():
    return (10, 5)

@pytest.fixture(scope = "function")
def reset_state():
    yield
    print("Clean up after test")

@pytest.mark.parametrize("a, b, expected",
                        [(2, 3, 5),
                        (0, 0, 0),
                        (-1, -1, -2)])
#add testing function
def test_add(a, b, expected):
    assert calculator.add(a,b) == expected

def test_subtract(numbers):
    a,b = numbers
    assert calculator.subtract(a, b) == 5

def test_divide(numbers):
    a, b  = numbers
    assert calculator.division(a,b) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.division(5, 0)

def test_multiply(reset_state):
    assert calculator.multiply(5, 3) == 15