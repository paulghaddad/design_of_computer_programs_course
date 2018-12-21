import itertools


def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state

    successor_states = {}
    actions = {'C': (0, 1), 'M': (1, 0), 'MC': (1, 1), 'CC': (0, 2), 'MM': (2, 0)}
    people_on_left, people_on_right = (M1, C1), (M2, C2)

    # If boat on left-hand side, we need to move people over to the right
    if B1:
        for action, (M, C) in actions.items():
            successor_state = (M1-M, C1-C, 0, M2+M, C2+C, 1)
            successor_states[successor_state] = action+'->'

    return successor_states
