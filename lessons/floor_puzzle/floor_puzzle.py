import itertools

def determine_floor_assignments():
    """
    Using a brute force approach, determine the floor assingments of five
    people: Hopper, Kay, Liskov, Perlis and Ritchie
    """
    floors = bottom_floor, _, _, _, top_floor = range(1, 6)
    orderings = itertools.permutations(floors, len(floors))

    return next(
        [Hopper, Kay, Liskov, Perlis, Ritchie]
        for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
        if Hopper != top_floor
        if Kay != bottom_floor
        if Liskov not in (bottom_floor, top_floor)
        if higher_floor(Perlis, Kay)
        if not adjacent_floor(Ritchie, Liskov)
        if not adjacent_floor(Liskov, Kay)
    )


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
