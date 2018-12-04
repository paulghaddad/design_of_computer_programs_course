import time
import pytest
import logging

from inverse_function import inverse

def square(x): return x*x


def test_inverse_function_small_x():
    sqrt = inverse(square)

    t0 = time.perf_counter()
    result = sqrt(100)
    t1 = time.perf_counter()

    logging.getLogger().info(f"The function took {t1-t0} seconds to perform")
    assert result == 10.0


def test_inverse_function_large_x():
    sqrt = inverse(square)

    t0 = time.perf_counter()
    result = sqrt(1000000000)
    t1 = time.perf_counter()

    logging.getLogger().info(f"The function took {t1-t0} seconds to perform")
    assert result == 10000.0
