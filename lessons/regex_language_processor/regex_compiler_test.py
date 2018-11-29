from regex_compiler import (
    alt,
    lit,
    star,
    oneof,
    match
)


def test_alt():
    g = alt(lit('a'), lit('b'))
    assert g('abc') == set(['bc'])


def test_match():
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(lit('hello'), 'hello how are you?') == 'hello'
    assert match(lit('x'), 'hello how are you?') == None
    assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
    assert match(oneof('xyz'), '   x is here!') == None
