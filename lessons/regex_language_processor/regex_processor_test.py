import pytest


from regex_processor import (
    match,
    search,
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


def test_match():
    assert match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
    assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
    assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'


def test_search():
    assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
