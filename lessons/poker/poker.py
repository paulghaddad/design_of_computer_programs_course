ACE_LOW_STRAIGHT = [14, 5, 4, 3, 2]


def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand, ...]"
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    max_hands, current_max_hand = [], iterable[0]
    key = key or (lambda x: x)

    for hand in iterable:
        if key(hand) > key(current_max_hand):
            current_max_hand = hand
            max_hands.clear()
            max_hands.append(hand)
        elif key(hand) == key(current_max_hand):
            max_hands.append(hand)

    return max_hands


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        # We only need the high card to break ties
        # A A A A 4 => (8, 14)
        return (8, max(ranks))
    elif kind(4, ranks):
        # kind must return the rank of the kind
        # 9 9 9 9 3 => (7, 9, 3)
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        pairs = two_pair(ranks)
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ["--23456789TJQKA".index(r) for r, s in cards]
    sorted_ranks = sorted(ranks, reverse=True)
    return [5, 4, 3, 2, 1] if (sorted_ranks == ACE_LOW_STRAIGHT) else sorted_ranks


def straight(ranks):
    "Return True if the ordered ranks from a 5-card straight"
    return ranks == [max(ranks) - rank for rank in range(5)]


def flush(hand):
    "Return True if all the cards have the same suit"
    suits = [s for r, s in hand]
    unique_suits = set(suits)
    return len(unique_suits) == 1


def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank

    return None


def two_pair(ranks):
    """
    If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None.
    """
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))

    if high_pair and low_pair and high_pair != low_pair:
        return (high_pair, low_pair)
    else:
        return None
