from regex_compiler import alt, lit


def test_alt():
    g = alt(lit('a'), lit('b'))
    assert g('abc') == set(['bc'])
