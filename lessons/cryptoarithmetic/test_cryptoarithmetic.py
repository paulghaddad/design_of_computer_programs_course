import pytest
from cryptoarithmetic import valid, solve


def test_valid_returns_true():
    assert valid('2 + 2 == 4') is True


def test_valid_returns_false():
    assert valid('2 + 2 == 5') is False


def test_valid_returns_false_on_zero_division_error():
    assert valid('2 / 0 == 5') is False


def test_valid_returns_false_on_invalid_numbers():
    assert valid('02 + 4 == 5') is False


def test_solve_with_solution():
    formula = "ODD + ODD == EVEN"
    assert solve(formula) == "122 + 122 == 3435"


def test_solve_with_no_solution():
    pass
