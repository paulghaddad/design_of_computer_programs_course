import pytest

from bridge_problem import bsuccessors

def test_bsuccessors():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == { (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}
