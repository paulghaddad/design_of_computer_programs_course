import re
import itertools

from poker import DEFAULT_DECK, hand_rank


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."

    best_hand = None

    # Take in hand and check for a black joker
    if '?B' in hand:
        # Generate all hand combinations when substituting a spade or club for the joker
        black_cards = [card for card in DEFAULT_DECK if re.search(r".[SC]", card)]

        for card in hand:
            if re.search(r".[SC]", card):
                hand_without_joker = hand[:]
                hand_without_joker.remove('?B')
                replacement_hands = [hand_without_joker + [black_card] for black_card in black_cards]

                for replacement_hand in replacement_hands:
                    best_hand_of_combination = max(itertools.combinations(replacement_hand, 5), key=hand_rank)

                    if not best_hand:
                        best_hand = best_hand_of_combination
                    elif best_hand_of_combination > best_hand:
                        best_hand = best_hand_of_combination
    elif '?R' in hand:
        # Generate all hand combinations when substituting a heart or diamond for the joker
        red_cards = [card for card in DEFAULT_DECK if re.search(r".[HD]", card)]

        for card in hand:
            if re.search(r".[HD]", card):
                hand_without_joker = hand[:]
                hand_without_joker.remove('?R')
                replacement_hands = [hand_without_joker + [red_card] for red_card in red_cards]

                for replacement_hand in replacement_hands:
                    best_hand_of_combination = max(itertools.combinations(replacement_hand, 5), key=hand_rank)

                    if not best_hand:
                        best_hand = best_hand_of_combination
                    elif best_hand_of_combination > best_hand:
                        best_hand = best_hand_of_combination

    return best_hand
