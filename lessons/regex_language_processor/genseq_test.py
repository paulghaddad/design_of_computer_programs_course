from genseq import (
    null,
    lit,
    alt,
    oneof,
    star,
    seq,
    plus,
    opt,
    genseq,
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


def test_genseq():
    x = lit('hi')
    y = lit('bye')
    Ns = range(11)

    assert genseq(x, y, Ns)


def test_gen():
    def N(hi): return set(range(hi+1))
    a,b,c = map(lit, 'abc')
    assert star(oneof('ab'))(N(2)) == set(['', 'a', 'aa', 'ab', 'ba', 'bb',
                                           'b'])
    assert(seq(star(a), seq(star(b), star(c)))(set([4])) == set(['aaaa', 'aaab',
                        'aaac', 'aabb', 'aabc', 'aacc', 'abbb', 'abbc',
                        'abcc', 'accc', 'bbbb', 'bbbc', 'bbcc', 'bccc', 'cccc']))

    assert(seq(plus(a), seq(plus(b), plus(c)))(set([5])) ==
           set(['aaabc', 'aabbc', 'aabcc', 'abbbc', 'abbcc', 'abccc']))


    assert(seq(oneof('bcfhrsm'), lit('at'))(N(3)) ==
           set(['bat', 'cat', 'fat', 'hat', 'mat', 'rat', 'sat']))

    assert(seq(star(alt(a, b)), opt(c))(set([3])) ==
           set(['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'baa', 'bab', 'bac',
                'bba', 'bbb', 'bbc']))

    assert lit('hello')(set([5])) == set(['hello'])
    assert lit('hello')(set([4])) == set()
    assert lit('hello')(set([6])) == set()
