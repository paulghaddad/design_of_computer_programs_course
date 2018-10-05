import itertools
import re

from poker import RED_DECK, BLACK_DECK, hand_rank

BLACK_JOKER = '?B'
RED_JOKER = '?R'


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."

    black_joker = _find_joker(hand, BLACK_JOKER)
    red_joker = _find_joker(hand, RED_JOKER)

    if black_joker:
        _remove_joker(hand, BLACK_JOKER)

    if red_joker:
        _remove_joker(hand, RED_JOKER)

    replacement_hands = [hand.copy()]

    for card in hand:
        if black_joker and red_joker:
            replacement_hands += [hand + [bc, rc] for bc in BLACK_DECK for rc in RED_DECK]
        elif red_joker:
            replacement_hands += [hand + [rc] for rc in RED_DECK]
        elif black_joker:
            replacement_hands += [hand + [bc] for bc in BLACK_DECK]

    return _find_best_hand(replacement_hands)


def _find_joker(hand, joker):
    """Return True if a joker is present that matches the card provided"""

    if joker in hand:
        return True
    else:
        return False


def _remove_joker(hand, joker):
    """Remove the desired joker from the hand"""

    hand.remove(joker)


def _find_best_hand(hands, key=hand_rank):
    """Find the highest 5 card hand of all combinations of 7 card hands"""

    best_hand = None
    for hand in hands:
        best_hand_of_combination = max(itertools.combinations(hand, 5), key=key)

        if not best_hand:
            best_hand = best_hand_of_combination
        elif best_hand_of_combination > best_hand:
            best_hand = best_hand_of_combination

    return best_hand
