from genseq import (
    null,
    lit,
    alt,
    oneof,
)


def test_lit():
    f = lit('hello')

    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4])) == null


def test_alt():
    g = alt(lit('hi'), lit('bye'))

    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])


def test_oneof():
    i = oneof('theseletters')

    assert i(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert i(set([2, 3, 4])) == null
