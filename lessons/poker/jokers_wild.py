import itertools
import re

from poker import RED_DECK, BLACK_DECK, hand_rank


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."

    best_hand, black_joker, red_joker= None, False, False
    if '?B' in hand:
        black_joker = True
        hand.remove('?B')

    if '?R' in hand:
        red_joker = True
        hand.remove('?R')

    if black_joker or red_joker:

        for card in hand:
            replacement_hands = [hand[:]]

            if re.search(r".[SC]", card):
                if black_joker:
                    replacement_hands += [hand + [black_card] for black_card in BLACK_DECK]


            if re.search(r".[HD]", card):
                if red_joker:
                    replacement_hands += [hand + [red_card] for red_card in RED_DECK]

            for replacement_hand in replacement_hands:
                best_hand_of_combination = max(itertools.combinations(replacement_hand, 5), key=hand_rank)

                if not best_hand:
                    best_hand = best_hand_of_combination
                elif best_hand_of_combination > best_hand:
                    best_hand = best_hand_of_combination

    return best_hand
