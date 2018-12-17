import itertools


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple, where here and there are frozensets of people (indicated by their times)
    and/or the 'light', and t is a number indicating the elapsed time. Action
    is represented as a tuple (person1, person2, arrow), where arrow is '->' for
    here to there and '<-' for there to here."""
    here, there, t = state

    # Determine where the light is
    direction_of_travel = '->' if 'light' in here else '<-'

    # Determine the people on the side with the light
    if direction_of_travel == '->':
        people_who_can_move = [person for person in here if person != 'light']
    else:
        people_who_can_move = [person for person in there if person != 'light']

    # Determine the combinations that can move and the end state
    combinations_of_travelers = itertools.combinations(people_who_can_move, 1)

    state_action_pairs = {}

    for combination in combinations_of_travelers:
        traveler = combination[0]
        there = frozenset((traveler, 'light'))
        here = frozenset(here - there)
        state_action_pairs[(here, there, t+1)] = (traveler, traveler, direction_of_travel)

    return state_action_pairs
