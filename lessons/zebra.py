import itertools

houses = [1, 2, 3, 4, 5]
orderings = itertools.permutations(houses)

for (red, green, ivory, yellow, blue) in orderings:
    for (Englishman, Spaniard, Ukranian, Japanese, Norweigian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
            for (coffee, tea, milk, oj, WATER) in orderings:
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                    # Constraint #2: The Englishman lives in the red house
                    if (red == Englishman): # Check to see if red and Englishman have been assigned the same house number
