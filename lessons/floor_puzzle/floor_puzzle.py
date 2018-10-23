from itertools import permutations


def determine_floor_assignments():
    """
    Using a brute force approach, determine the floor assingments of five
    people: Hopper, Kay, Liskov, Perlis and Ritchie
    """
    floors = range(1, 6)

    floor_assignment_permutations = permutations(floors, 5)

    for hopper, kay, liskov, perlis, ritchie in floor_assignment_permutations:
        if hopper != 5:
            if kay != 1:
                if liskov not in (1, 5):
                    if higher_floor(perlis, kay):
                        if not adjacent_floor(ritchie, liskov):
                            if not adjacent_floor(liskov, kay):
                                return hopper, kay, liskov, perlis, ritchie


def higher_floor(person_1, person_2):
    """
    Returns True if person_1 lives on a higher floor than person_2. Otherwise,
    returns False.
    """
    return person_1 > person_2


def adjacent_floor(person_1, person_2):
    """
    Returns True if person_1 lives on a floor immediately above or below
    person_2.
    """
    return abs(person_1 - person_2) == 1
