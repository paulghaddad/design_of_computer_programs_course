def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = matchset(pattern, text)
    if remainders:
        shortest = min(remainders, key=len)
        # we can do the following since the match must start at the start of the
        # text
        return text[:len(text) - len(shortest)]


def search(pattern, text):
    "Match pattern anywhere in text; return longest earliest match or None."
    for i in range(len(text)):
        m = match(pattern, text[i:])
        # we can't just do if m because the empty string may be the match and
        # that's Falsey. So we need to explicitly compare against None.
        if m is not None:
            return m


def lit(string):
    return ('lit', string)


def seq(x, y):
    return ('seq', x, y)


def alt(x, y):
    return ('alt', x, y)


def star(x):
    return ('star', x)


def plus(x):
    return seq(x, star(x))


def opt(x):
    return alt(lit(''), x)


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
