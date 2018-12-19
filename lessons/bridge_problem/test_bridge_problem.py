import pytest

from bridge_problem import (
    bcost,
    bridge_problem,
    bsuccessors,
    bsuccessors2,
    path_actions,
    path_cost,
    path_states,
)

def test_bsuccessors():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == { (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={ (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}


def test_bsuccessors2():
    here1 = frozenset([1, 'light'])
    there1 = frozenset([])

    assert bsuccessors2((here1, there1)) == {(frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])

    assert bsuccessors2((here2, there2)) == {(frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'), (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'), (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}


def test_path_cost():
    assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
    assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3')) == 6


def test_bcost():
    assert bcost((4, 2, '->'),) == 4
    assert bcost((3, 10, '<-'),) == 10


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
    assert bridge_problem([1,2,5,10]) == [(frozenset({1, 2, 5, 'light', 10}), frozenset(), 0), (2, 1, '->'),
     (frozenset({10, 5}), frozenset({1, 2, 'light'}), 2), (1, 1, '<-'),
     (frozenset({1, 10, 5, 'light'}), frozenset({2}), 3), (5, 10, '->'),
     (frozenset({1}), frozenset({2, 10, 5, 'light'}), 13), (2, 2, '<-'),
     (frozenset({1, 2, 'light'}), frozenset({10, 5}), 15), (2, 1, '->'),
     (frozenset(), frozenset({1, 2, 5, 'light', 10}), 17)]


def test_bridge_problem_finds_cheapest_solution():
    assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2 # the [-1][-1] grabs the total elapsed time
    assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17
