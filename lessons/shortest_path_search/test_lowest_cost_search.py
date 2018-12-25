import pytest

from lowest_cost_search import bridge_problem3


def test_lowest_cost_search():
    here = [1, 2, 5, 10]

    assert bridge_problem3(here) == [
                (frozenset([1, 2, 'light', 10, 5]), frozenset([])), 
                ((2, 1, '->'), 2), 
                (frozenset([10, 5]), frozenset([1, 2, 'light'])), 
                ((2, 2, '<-'), 4), 
                (frozenset(['light', 10, 2, 5]), frozenset([1])), 
                ((5, 10, '->'), 14), 
                (frozenset([2]), frozenset([1, 10, 5, 'light'])), 
                ((1, 1, '<-'), 15), 
                (frozenset([1, 2, 'light']), frozenset([10, 5])), 
                ((2, 1, '->'), 17), 
                (frozenset([]), frozenset([1, 10, 2, 5, 'light']))]
