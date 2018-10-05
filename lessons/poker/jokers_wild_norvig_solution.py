import itertools

from poker import RED_DECK, BLACK_DECK, hand_rank
from seven_card_stud import best_hand


def best_wild_hand_norvig(hand):
    "Try all values for jokers in all 5-card selections."
    hands = set(best_hand(h)
                for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)


def replacements(card):
    """Return a list of the possible replacements for a card.
    There will be more than 1 only for wild cards."""
    if card == '?B': return BLACK_DECK
    elif card == '?R': return RED_DECK
    else: return [card]
