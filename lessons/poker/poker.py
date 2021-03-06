import random
import re

ACE_LOW_STRAIGHT = [14, 5, 4, 3, 2]
DEFAULT_DECK = [r + s for r in "23456789TJQKA" for s in "SHDC"]
RED_DECK = [card for card in DEFAULT_DECK if re.search(r".[HD]", card)]
BLACK_DECK = [card for card in DEFAULT_DECK if re.search(r".[SC]", card)]
COUNT_RANKINGS = {
    (5,): 10,
    (4, 1): 7,
    (3, 2): 6,
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0,
}


def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand, ...]"
    return allmax(hands, key=hand_rank)


def deal(numhands, n=5, deck=DEFAULT_DECK):
    """Return a list of numhands of hands consisting of n cards"""
    dealt_hands = []
    random.shuffle(deck)

    return [deck[i * n : i * n + n] for i in range(numhands)]


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    max_hands, max_hand_value = [], None
    key = key or (lambda x: x)

    for hand in iterable:
        hand_value = key(hand)
        if not max_hands or hand_value > max_hand_value:
            max_hands, max_hand_value = [hand], key(hand)
        elif hand_value == max_hand_value:
            max_hands.append(hand)

    return max_hands


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    # counts is the count of each rank; rank lists corresponding ranks
    # E.g, '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(["--23456789TJQKA".index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r, s in hand])) == 1

    return max(COUNT_RANKINGS[counts], 4 * straight + 5 * flush), ranks


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ["--23456789TJQKA".index(r) for r, s in cards]
    sorted_ranks = sorted(ranks, reverse=True)
    return [5, 4, 3, 2, 1] if (sorted_ranks == ACE_LOW_STRAIGHT) else sorted_ranks


def group(items):
    """
    Return a list of [(count, x)...], highest count first, then highest x first.
    """
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs):
    return zip(*pairs)
