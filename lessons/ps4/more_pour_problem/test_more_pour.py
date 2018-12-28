import pytest

from more_pour import more_pour_problem

def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [(0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
