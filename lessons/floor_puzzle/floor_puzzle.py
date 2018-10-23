from itertools import permutations


def determine_floor_assignments():
    """
    Using a brute force approach, determine the floor assingments of five
    people: Hopper, Kay, Liskov, Perlis and Ritchie
    """
    floors = range(1, 6)

    floor_assignment_permutations = permutations(floors, 5)

    for hopper, kay, liskov, perlis, ritchie in floor_assignment_permutations:
        print(hopper, kay, liskov, perlis, ritchie)
