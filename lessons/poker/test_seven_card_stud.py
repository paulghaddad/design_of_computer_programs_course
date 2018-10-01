import pytest

from seven_card_stud import best_hand

def test_best_hand():
    assert sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) == ["6C", "7C", "8C", "9C", "10C"]
    assert sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) == ["8C", "8S", "TC", "TD", "TH"]
    assert sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) == ["7C", "7D", "7H", "7S", "TD"]
