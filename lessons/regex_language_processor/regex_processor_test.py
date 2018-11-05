import pytest


from regex_processor import (
    matchset,
    lit,
    seq,
    alt,
    star,
    plus,
    opt,
    oneof,
)


def test_lit():
    assert lit('abc') == ('lit', 'abc')


def test_seq():
    assert seq(('lit', 'a'), ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))


def test_alt():
    assert alt(('lit', 'a'), ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))


def test_star():
    assert star(('lit', 'a')) == ('star', ('lit', 'a'))


def test_plus():
    assert plus(('lit', 'c')) == ('seq', ('lit', 'c'), ('star', ('lit', 'c')))


def test_opt():
    assert opt(('lit', 'x')) == ('alt', ('lit', ''), ('lit', 'x'))


def test_oneof():
    assert oneof('abc') == ('oneof', ('a', 'b', 'c'))


def test_matchset():
    assert matchset(('lit', 'abc'), 'abcdef') == set(['def'])
    assert matchset(('seq', ('lit', 'hi '), ('lit', 'there ')), 'hi there nice to meet you') == set(['nice to meet you'])
    assert matchset(('alt', ('lit', 'dog'), ('lit', 'cat')), 'dog and cat') == set([' and cat'])
    assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
    assert matchset(('oneof', 'a'), 'aabc123') == set(['abc123'])
    assert matchset(('eol',),'') == set([''])
    assert matchset(('eol',),'not end of line') == frozenset([])
    assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])


# def test_search():
#     a,b,c = lit('a'), lit('b'), lit('c')
#     abcstars = seq(star(a), seq(star(b), star(c)))
#     dotstar = star(dot)
#     assert search(lit('def'), 'abcdefg') == 'def'
#     assert search(seq(lit('def'), eol), 'abcdef') == 'def'
#     assert search(seq(lit('def'), eol), 'abcdefg') is None
#     assert search(a, 'not the start') == 'a'
#     assert match(a, 'not the start') is None
#     assert match(abcstars, 'aaabbbccccccccdef') == 'aaabbbccccccccdef'
#     assert match(abcstars, 'junk') == ''
#     assert all(match(seq(abcstars, eol), s) == s for s in 'abc aaabbccc aaaabcccc'.split())
#     r = seq(lit('ab'), seq(dotstar, seq(lit('aca'), seq(dotstar, seq(a, eol)))))
#     assert all(search(r, s) is not None for s in 'abracadabra abacaa about-acacia-flora'.split())
#     assert all(match(seq(c, seq(dotstar, b)), s) is not None for s in 'cab cob carob cb carbuncle'.split())
#     assert not any(match(seq(c, seq(dot, b)), s) for s in 'crab cb across scab'.split())
