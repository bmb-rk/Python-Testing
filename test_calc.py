import pytest
from calc import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-4, 2) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
