import pytest


from missionaries_and_cannibals import csuccessors


def test_csuccessors():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}

    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                                (2, 1, 1, 3, 3, 0): '<-M',
                                                (3, 1, 1, 2, 3, 0): '<-MM',
                                                (1, 3, 1, 4, 1, 0): '<-CC',
                                                (2, 2, 1, 3, 2, 0): '<-MC'}

    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
