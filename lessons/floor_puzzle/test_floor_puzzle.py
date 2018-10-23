import pytest


from floor_puzzle import determine_floor_assignments, higher_floor, adjacent_floor


def test_determine_floor_assignments():
    assert determine_floor_assignments() == [3, 2, 4, 5, 1]


def test_higher_floor_when_first_person_on_higher_floor():
    assert higher_floor(5, 1) is True


def test_higher_floor_when_first_person_on_lower_floor():
    assert higher_floor(1, 5) is False


def test_adjacent_floor_when_true():
    assert adjacent_floor(2, 3) is True


def test_adjacent_floor_when_false():
    assert adjacent_floor(2, 4) is False
