def my_csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state

    # Check if cannibals can dine in the current state -> no successors
    # Also check that there's at least one missionary
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}

    actions = {'C': (0, 1), 'M': (1, 0), 'MC': (1, 1), 'CC': (0, 2), 'MM': (2, 0)}

    successor_states = {}
    # If boat on left-hand side, we need to move people over to the right
    if B1:
        for action, (M, C) in actions.items():
            if M1-M >= 0 and C1-C >= 0:
                successor_state = (M1-M, C1-C, 0, M2+M, C2+C, 1)
                successor_states[successor_state] = action+'->'
    # If boat on right-hand side, we need to move people over to the left
    else:
        for action, (M, C) in actions.items():
            if M2-M >= 0 and C2-C >= 0:
                successor_state = (M1+M, C1+C, 1, M2-M, C2-C, 0)
                successor_states[successor_state] = '<-'+action

    return successor_states


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
