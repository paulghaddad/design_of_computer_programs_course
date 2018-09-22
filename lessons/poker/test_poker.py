import pytest
from poker import poker, hand_rank, card_ranks, straight, flush, kind, two_pair


@pytest.mark.skip()
def test_poker():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    # Test extreme values
    assert poker([fh]) == fh
    assert poker([sf] + 99 * [fh]) == sf


def test_hand_rank():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    flush = "10H 8H 7H 5H 3H".split()
    straight = "JD 10S 9C 8D 7H".split()
    three_kind = "7C 7D 7H 5H 2S".split()
    two_pair = "JC JD 3H 3S KS".split()
    pair = "2S 2C JC 6S 3H".split()
    high_card = "7H 5S 4D 3C 2H".split()

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(flush) == (5, [10, 8, 7, 5, 3])
    assert hand_rank(straight) == (4, 11)
    assert hand_rank(three_kind) == (3, 7, [7, 7, 7, 5, 2])
    assert hand_rank(two_pair) == (2, 11, 3, [13, 11, 11, 3, 3])
    assert hand_rank(pair) == (1, 2, [11, 6, 3, 2, 2])
    assert hand_rank(high_card) == (0, [7, 5, 4, 3, 2])


def test_card_ranks():
    """
    card_ranks returns the ranks in sorted order
    """
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]


def test_straight():
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False


def test_ace_low_straight():
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
    assert straight(card_ranks(al)) is True


def test_flush():
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    assert flush(sf) == True
    assert flush(fk) == False


def test_kind():
    fk = "9D 9H 9S 9C 7D".split()
    fk_ranks = card_ranks(fk)

    assert kind(4, fk_ranks) == 9
    assert kind(3, fk_ranks) is None
    assert kind(2, fk_ranks) is None
    assert kind(1, fk_ranks) == 7


def test_two_pair():
    tp = "TD 7H TH 7C 3S".split()
    fk = "9D 9H 9S 9C 7D".split()
    op = "9J 9H 8D 5S 2H".split()
    tp_ranks = card_ranks(tp)
    fk_ranks = card_ranks(fk)
    op_ranks = card_ranks(op)

    assert two_pair(tp_ranks) == (10, 7)
    assert two_pair(fk_ranks) is None
    assert two_pair(op_ranks) is None
