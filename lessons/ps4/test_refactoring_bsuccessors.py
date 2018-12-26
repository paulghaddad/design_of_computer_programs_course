import pytest

from refactoring_bsuccessors import bsuccessors3

def test_bsuccessors3():
    assert bsuccessors3((frozenset([1]), frozenset([]), 0)) == {
        (frozenset([]), frozenset([1]), 1)  :  (set([1]), '->')
    }
