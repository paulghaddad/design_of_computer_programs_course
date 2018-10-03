import itertools
from poker import allmax, hand_rank


def best_hand(hand, n=5):
    """From a 7-card hand, return the best 5 card hand."""
    five_card_combinations = itertools.combinations(hand, n)

    best_hands = [list(hand) for hand in allmax(five_card_combinations, key=hand_rank)]
    return best_hands[0]
