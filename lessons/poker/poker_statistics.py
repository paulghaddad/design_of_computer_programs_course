from poker import deal, hand_rank


def hand_percentages(n=700 * 1000):
    """
    Sample n random hands and print a table of percentages for each hand.
    """
    counts = [0] * 9
    for i in range(n // 10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1

    hand_names = [
        "Straight Flush",
        "4 Kind",
        "Full House",
        "Flush",
        "Straight",
        "3 Kind",
        "2 Pair",
        "Pair",
        "High Card",
    ]

    for i in reversed(range(9)):
        print(f"{hand_names[i]}: {round(counts[i]/n * 100, 2)}%")


hand_percentages()
