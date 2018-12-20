def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple, where here and there are frozensets of people (indicated by their times)
    and/or the 'light', and t is a number indicating the elapsed time. Action
    is represented as a tuple (person1, person2, arrow), where arrow is '->' for
    here to there and '<-' for there to here."""
    here, there, t = state

    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                    (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')


def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    here, there = state

    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light'])),
                      (a, b, '->'))
                     for a in here if a is not 'light'
                     for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light'])),
                      (a, b, '<-'))
                     for a in there if a is not 'light'
                     for b in there if b is not 'light')


def path_cost(path):
    """
    The total cost of a path (which is stored in a tuple
    with the final action.

    path = (state, (action, total_cost), state, ... )
    """
    if len(path) < 3: # we don't have an action, just an individual state
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost


def bcost(action):
    """Returns the cost (a number) of an action in the bridge problem."""
    a, b, arrow = action
    return max(a, b)


def path_states(path):
    "Return a list of states in this path."
    return path[::2]


def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


def bridge_problem(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        here1, there1, t1 = state1 = path[-1]
        if not here1 or there1 == set(['light']):
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=elapsed_time)

    return []


def bridge_problem2(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people-here, people-there) tuple
    # e.g. ({1, 2, 5, 10, 'light'}, {})
    frontier = [ [(here, frozenset())] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1 = state1 = final_state(path)
        if not here1 or (len(here1) == 1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors2(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail


Fail = None


def final_state(path): return path[-1]


def add_to_frontier(frontier, path):
    "Add path to frontier, replacing costlier path if there is one."
    # (This could be done more efficiently.)
    # Find if there is an old path to the final state of this path.
    old = None
    for i,p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return # Old path was better; do nothing
    elif old is not None:
        del frontier[old] # Old path was worse; delete it
    # Now add the new path and resort
    frontier.append(path)


def elapsed_time(path):
    return path[-1][2]


class TestBridge: """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> path_states(bridge_problem([1,2,5,10,15,20]))
[(frozenset([1, 2, 20, 5, 'light', 10, 15]), frozenset([]), 0), (frozenset([10, 20, 5, 15]), frozenset([1, 2, 'light']), 2), (frozenset([1, 20, 5, 'light', 10, 15]), frozenset([2]), 3), (frozenset([1, 20, 15]), frozenset(['light', 2, 10, 5]), 13), (frozenset([1, 2, 'light', 20, 15]), frozenset([10, 5]), 15), (frozenset([20, 15]), frozenset([1, 10, 2, 5, 'light']), 17), (frozenset([1, 'light', 20, 15]), frozenset([10, 2, 5]), 18), (frozenset([1]), frozenset([2, 20, 5, 'light', 10, 15]), 38), (frozenset([1, 2, 'light']), frozenset([10, 20, 5, 15]), 40), (frozenset([]), frozenset([1, 2, 20, 5, 'light', 10, 15]), 42)]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (1, 2, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> path_states(bridge_problem([1,2,4,8,16,32]))
[(frozenset([32, 1, 2, 4, 16, 8, 'light']), frozenset([]), 0), (frozenset([32, 16, 4, 8]), frozenset([1, 2, 'light']), 2), (frozenset([32, 16, 4, 1, 8, 'light']), frozenset([2]), 3), (frozenset([32, 16, 1]), frozenset([8, 'light', 2, 4]), 11), (frozenset([32, 16, 2, 'light', 1]), frozenset([8, 4]), 13), (frozenset([32, 16]), frozenset([8, 1, 2, 4, 'light']), 15), (frozenset([32, 16, 'light', 1]), frozenset([8, 2, 4]), 16), (frozenset([1]), frozenset([32, 16, 2, 4, 8, 'light']), 48), (frozenset([1, 2, 'light']), frozenset([32, 16, 4, 8]), 50), (frozenset([]), frozenset([32, 16, 2, 4, 1, 8, 'light']), 52)]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
