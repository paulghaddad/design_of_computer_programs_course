import logging
import math
import pytest
import time

from inverse_function import inverse

def square(x): return x*x
sqrt = inverse(square)


def power10(x): return 10**x
log10 = inverse(power10)


def cube(x): return x**3
cuberoot = inverse(cube)


def test_inverse_function_small_x():
    t0 = time.perf_counter()
    result = sqrt(100)
    t1 = time.perf_counter()

    logging.getLogger().info(f"The function took {t1-t0} seconds to perform")

    assert abs(result - 10.0) < 1/128


def test_inverse_function_large_x():
    sqrt = inverse(square)

    t0 = time.perf_counter()
    result = sqrt(1000000000)
    t1 = time.perf_counter()

    logging.getLogger().info(f"The function took {t1-t0} seconds to perform")
    assert abs(result - 31622.77) < 1/128


# def test_all_functions():
#     nums = [2, 4, 6, 8, 10, 99, 100, 101, 1000, 10000, 20000, 40000, 1000000000]
#     for n in nums:
#         expected = sqrt(n)
#         actual = sqrt(n)
#
#         diff = abs(actual - expected)
#         assert diff < .002
#         test1(n, 'sqrt', sqrt(n), math.sqrt(n))
#         # test1(n, 'log', log10(n), math.log10(n))
#         # test1(n, '3-rt', cuberoot(n), n**(1./3.))
