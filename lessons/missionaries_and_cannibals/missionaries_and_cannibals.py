def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state

    # Check if cannibals can dine in the current state -> no successors
    if C1 > M1 or C2 > M2:
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
