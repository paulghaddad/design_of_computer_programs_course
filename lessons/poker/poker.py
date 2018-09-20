def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


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
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    return sorted(ranks, reverse=True)


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
