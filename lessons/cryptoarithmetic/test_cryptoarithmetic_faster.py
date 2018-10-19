import pytest
from cryptoarithmetic_faster import solve


def test_solve_with_solution():
    formula = "ODD + ODD == EVEN"
    assert solve(formula) == "655 + 655 == 1310"
