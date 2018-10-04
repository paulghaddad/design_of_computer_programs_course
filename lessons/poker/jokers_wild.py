import itertools
import re

from poker import RED_DECK, BLACK_DECK, hand_rank


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."

    best_hand, black_joker, red_joker = None, False, False
    if '?B' in hand:
        black_joker = True
        hand.remove('?B')

    if '?R' in hand:
        red_joker = True
        hand.remove('?R')

    replacement_hands = [hand[:]]
    if black_joker or red_joker:
        for card in hand:
            if black_joker and red_joker:
                replacement_hands += [hand + [black_card, red_card] for black_card in BLACK_DECK if black_joker for red_card in RED_DECK]
            elif red_joker:
                replacement_hands += [hand + [red_card] for red_card in RED_DECK]
            elif black_joker:
                replacement_hands += [hand + [black_card] for black_card in BLACK_DECK]

    for replacement_hand in replacement_hands:
        best_hand_of_combination = max(itertools.combinations(replacement_hand, 5), key=hand_rank)

        if not best_hand:
            best_hand = best_hand_of_combination
        elif best_hand_of_combination > best_hand:
            best_hand = best_hand_of_combination

    return best_hand
