import itertools

TOP_FLOOR = 5
BOTTOM_FLOOR = 1


def determine_floor_assignments():
    """
    Using a brute force approach, determine the floor assingments of five
    people: Hopper, Kay, Liskov, Perlis and Ritchie
    """
    floors = range(BOTTOM_FLOOR, TOP_FLOOR + 1)

    return next(
        [Hopper, Kay, Liskov, Perlis, Ritchie]
        for (Hopper, Kay, Liskov, Perlis, Ritchie) in itertools.permutations(
            floors, len(floors)
        )
        if Hopper != TOP_FLOOR
        if Kay != BOTTOM_FLOOR
        if Liskov not in (BOTTOM_FLOOR, TOP_FLOOR)
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
