import pytest

from inverse_function import inverse

def square(x): return x*x

def test_inverse_function():
    sqrt = inverse(square)

    assert sqrt(100) == 10.0 
