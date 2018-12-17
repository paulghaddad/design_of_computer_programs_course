import pytest

from bridge_problem import bsuccessors

def test_bsuccessors():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == { (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={ (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
