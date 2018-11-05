def lit(string):
    return ('lit', string)


def seq(*sequences):
    return ('seq', *sequences)


def alt(*strings):
    return ('alt', *strings)


def star(character):
    return ('star', character)


def plus(literal):
    return ('seq', ('lit', literal[1]), ('star', ('lit', literal[1])))


def opt(literal):
    return ('alt', lit(''), literal)


def oneof(chars):
    return ('oneof', tuple(chars))


dot = ('dot',)
eol = ('eol',)


def matchset(pattern, text):
    """
    Match pattern at start of text; return a set of remainders of text.
    """
    null = frozenset()

    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text) # union of these matched sets
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        return set([text[1:]]) if text.startswith(x) else null
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError(f"unknown pattern: {pattern}")


def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y
