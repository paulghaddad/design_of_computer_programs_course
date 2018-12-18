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


def path_states(path):
    "Return a list of states in this path."
    states = []
    for i, element in enumerate(path):
        if i % 2 == 0:
            states.append(element)

    return states


def path_actions(path):
    "Return a list of actions in this path."
    actions = []
    for i, element in enumerate(path):
        if i % 2 != 0:
            actions.append(element)

    return actions
