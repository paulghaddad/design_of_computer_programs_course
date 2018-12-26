import pytest

from refactoring_bsuccessors import bsuccessors3

def test_bsuccessors3():
    assert bsuccessors3((frozenset([1]), frozenset([]), 0)) == {
        (frozenset([]), frozenset([1]), 1)  :  (set([1]), '->')
    }

    assert bsuccessors3((frozenset([1, 2]), frozenset([]), 0)) == {
                    (frozenset([1]), frozenset([2]), 1)    :  (set([2]), '->'), 
                    (frozenset([]), frozenset([1, 2]), 1)  :  (set([1, 2]),
                                                               '->'), 
                    (frozenset([2]), frozenset([1]), 1)    :  (set([1]), '->')
    }

    assert bsuccessors3((frozenset([2, 4]), frozenset([3, 5]), 1)) == {
                    (frozenset([2, 4, 5]), frozenset([3]), 0)   :  (set([5]),
                                                                    '<-'), 
                    (frozenset([2, 3, 4, 5]), frozenset([]), 0) :  (set([3, 5]),
                                                                    '<-'), 
                    (frozenset([2, 3, 4]), frozenset([5]), 0)   :  (set([3]),
                                                                    '<-')
    }
