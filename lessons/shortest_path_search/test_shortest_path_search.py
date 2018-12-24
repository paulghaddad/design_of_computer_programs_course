from shortest_path_search import shortest_path_search


# Let's say the states in an optimization problem are given by integers.
# From a state, i, the only possible successors are i+1 and i-1. Given
# a starting integer, find the shortest path to the integer 8. 
#
# This is an overly simple example of when we can use the 
# shortest_path_search function. We just need to define the appropriate
# is_goal and successors functions.


def is_goal(state):
    if state == 8:
        return True
    else:
        return False


def successors(state):
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors


def test_shortest_path_search():
    assert shortest_path_search(5, successors, is_goal) == [5, '->', 6, '->', 7, '->', 8]


# Tests for solving the Missionaries and Cannibals problem with the general
# solution

def test_missionaries_and_cannibals():
    assert mc_problem2(start=(1, 1, 1, 0, 0, 0)) == [ (1, 1, 1, 0, 0, 0), 'MC->', (0, 0, 0, 1, 1, 1)]
    assert mc_problem2() == [(3, 3, 1, 0, 0, 0), 'CC->',
                             (3, 1, 0, 0, 2, 1), '<-M',
                             (4, 1, 1, -1, 2, 0), 'MC->',
                             (3, 0, 0, 0, 3, 1), '<-C',
                             (3, 1, 1, 0, 2, 0), 'MM->',
                             (1, 1, 0, 2, 2, 1), '<-MC',
                             (2, 2, 1, 1, 1, 0), 'MM->',
                             (0, 2, 0, 3, 1, 1), '<-C',
                             (0, 3, 1, 3, 0, 0), 'CC->',
                             (0, 1, 0, 3, 2, 1), '<-M',
                             (1, 1, 1, 2, 2, 0), 'MC->',
                             (0, 0, 0, 3, 3, 1)]


def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
    if goal is None:
        goal = (0, 0, 0) + start[:3]

    def is_goal(state):
        return state == goal

    return shortest_path_search(start, csuccessors, is_goal)


def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state

    # Check if cannibals can dine in the current state -> no successors
    # Also check that there's at least one missionary
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}

    items = []
    if B1 > 0:
        items += [(sub(state, delta), a+'->') for delta, a in deltas.items()]

    if B2 > 0:
        items += [(add(state, delta), '<-'+a) for delta, a in deltas.items()]

    return dict(items)


deltas = {
    (2, 0, 1,     -2, 0, -1): 'MM',
    (0, 2, 1,     0, -2, -1): 'CC',
    (1, 1, 1,    -1, -1, -1): 'MC',
    (1, 0, 1,    -1, 0, -1):  'M',
    (0, 1, 1,    0, -1, -1):  'C',
}


def add(X, Y):
    "Add two vectors, X and Y."
    return tuple(x+y for x,y in zip(X, Y))


def sub(X, Y):
    "Subtract vector Y from X."
    return tuple(x-y for x,y in zip(X, Y))
