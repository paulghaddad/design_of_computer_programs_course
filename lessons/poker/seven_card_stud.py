import itertools
from poker import hand_rank


def best_hand(hand, n=5):
    """From a 7-card hand, return the best 5 card hand."""
    combinations = itertools.combinations(hand, n)

    return max(combinations, key=hand_rank)
