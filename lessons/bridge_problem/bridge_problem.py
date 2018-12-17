import itertools


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple, where here and there are frozensets of people (indicated by their times)
    and/or the 'light', and t is a number indicating the elapsed time. Action
    is represented as a tuple (person1, person2, arrow), where arrow is '->' for
    here to there and '<-' for there to here."""
    here, there, t = state

    direction_of_travel = '->' if 'light' in here else '<-'

    if direction_of_travel == '->':
        people_who_can_move = [person for person in here if person != 'light']
    else:
        people_who_can_move = [person for person in there if person != 'light']

    combinations_of_travelers = itertools.combinations(people_who_can_move, 1)

    state_action_pairs = {}
    for combination in combinations_of_travelers:
        traveler = combination[0]
        if direction_of_travel == '->':
            there = frozenset((traveler, 'light'))
            here = frozenset(here - there)
        else:
            here = frozenset((traveler, 'light'))
            there = frozenset(there - here)

        elapsed_time = t + traveler
        state_action_pairs[(here, there, elapsed_time)] = (traveler, traveler, direction_of_travel)

    return state_action_pairs
