import calc
import pytest

def test_add():
    result = calc.add(3,2)
    assert result == 5

def test_subtract():
    result = calc.subtract(4,3)
    assert result == 1

def test_multiply():
    result = calc.multiply(5,4)
    assert result == 20

def test_divide():
    result = calc.divide(20,4)
    assert result == 5

# @pytest.mark.parametrize(z)
# def test_square(user_inp,expected):
#     result = calc.square(user_inp)
#     assert result == expected

