import pytest

from jokers_wild import best_wild_hand
from jokers_wild_norvig_solution import best_wild_hand_norvig


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())) == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("6H 7H 8H 9H TH 5H ?R".split())) == ['7H', '8H', '9H', 'JH', 'TH'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split())) == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split())) == ['7C', '7D', '7H', '7S', 'JD'])


def test_best_wild_hand_norvigs_solution():
    assert (sorted(best_wild_hand_norvig("6C 7C 8C 9C TC 5C ?B".split())) == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand_norvig("6H 7H 8H 9H TH 5H ?R".split())) == ['7H', '8H', '9H', 'JH', 'TH'])
    assert (sorted(best_wild_hand_norvig("TD TC 5H 5C 7C ?R ?B".split())) == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand_norvig("JD TC TH 7C 7D 7S 7H".split())) == ['7C', '7D', '7H', '7S', 'JD'])
