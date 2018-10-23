import pytest


from floor_puzzle import determine_floor_assignments


def test_determine_floor_assignments():
    assert determine_floor_assignments() == ('Liskov', 'Kay', 'Hopper', 'Ritchie', 'Perlis')
