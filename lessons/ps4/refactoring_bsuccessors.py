# In this problem you will be refactoring the bsuccessors function.
# Your new function, bsuccessors3, will take a state as an input
# and return a dict of {state:action} pairs. 
#
# A state is a (here, there, light) tuple. Here and there are 
# frozensets of people (each person is represented by an integer
# which corresponds to their travel time), and light is 0 if 
# it is on the `here` side and 1 if it is on the `there` side.
#
# An action is a tuple of (travelers, arrow), where the arrow is
# '->' or '<-'. See the test() function below for some examples
# of what your function's input and output should look like.

def bsuccessors3(state):
    """
    Return a dict of {state:action} pairs.  State is (here, there, light)
    where here and there are frozen sets of people, light is 0 if the light is
    on the here side and 1 if it is on the there side.
    Action is a tuple (travelers, arrow) where arrow is '->' or '<-'
    """
    here, there, light = state

    if light:
        return dict(((here | frozenset([a, b]),
                      there - frozenset([a, b]),
                      0), (set([a, b]), '<-'))
                    for a in there
                    for b in there)
    else:
        return dict(((here - frozenset([a, b]),
                      there | frozenset([a, b]),
                      1), (set([a, b]), '->'))
                    for a in here
                    for b in here)

def bsuccessors3_norvig(state):
    _, _, light = state
    return dict(bsuccessor3_norvig(state, set([a, b]))
                for a in state[light]
                for b in state[light])

def bsuccessor3_norvig(state, travelers):
    "The single successor state when this set of travelers move."
    _, _, light = state
    start = state[light] - travelers
    dest = state[1-light] | travelers

    if light == 0:
        return (start, dest, 1), (travelers, '->')
    else:
        return (dest, start, 0), (travelers, '<-')
