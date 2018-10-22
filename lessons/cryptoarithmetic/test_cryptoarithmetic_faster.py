import pytest
from cryptoarithmetic_faster import solve


def test_solve_with_solution():
    formula = "ODD + ODD == EVEN"
    assert solve(formula) == "655 + 655 == 1310"


def test_compile_formula_with_leading_zeros():
    assert solve('A + B == BA') == None # should NOT return '1 + 0 == 01'
    assert solve('YOU == ME**2') in ('324 == 18**2', '289 == 17**2', '576 == 24**2', '841 == 29**2')
    assert solve('X / X == X') == '1 / 1 == 1'
