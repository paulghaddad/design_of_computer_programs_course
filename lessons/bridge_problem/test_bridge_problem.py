import pytest

from bridge_problem import (
    bsuccessors,
    path_states,
    path_actions,
    bridge_problem,
)

def test_bsuccessors():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == { (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={ (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}


testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5),     # state 1
                (5, 2, '->'),                                        # action 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (2, 1, '->'),                                        # action 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (5, 5, '->'), 
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (5, 10, '->'), 
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (2, 2, '->'), 
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (10, 1, '->'), 
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (10, 10, '->'), 
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (10, 2, '->'), 
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (5, 1, '->'), 
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
                (1, 1, '->')]

def test_path_states():
    assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]


def test_path_actions():
    assert path_actions(testpath) == [(5, 2, '->'), # action 1
                                      (2, 1, '->'), # action 2
                                      (5, 5, '->'),
                                      (5, 10, '->'),
                                      (2, 2, '->'),
                                      (10, 1, '->'),
                                      (10, 10, '->'),
                                      (10, 2, '->'),
                                      (5, 1, '->'),
                                      (1, 1, '->')]


def test_bridge_problem():
    assert bridge_problem([1,2,5,10]) == [(frozenset({1, 2, 'light', 5, 10}), frozenset(), 0), (2, 1, '->'),
        (frozenset({10, 5}), frozenset({1, 2, 'light'}), 2), (1, 1, '<-'),
        (frozenset({1, 10, 'light', 5}), frozenset({2}), 3), (5, 1, '->'),
        (frozenset({10}), frozenset({1, 2, 'light', 5}), 8), (1, 1, '<-'),
        (frozenset({1, 10, 'light'}), frozenset({2, 5}), 9), (10, 1, '->'),
        (frozenset(), frozenset({1, 2, 'light', 5, 10}), 19)]


    assert bridge_problem([1,2,5,10])[1::2] == [(2, 1, '->'), (1, 1, '<-'), (5, 1, '->'), (1, 1, '<-'), (10, 1, '->')]

