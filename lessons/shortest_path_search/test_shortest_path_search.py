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
