null = frozenset([])


def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null


def alt(x, y): return lambda Ns: x(Ns) | y(Ns)


def star(x): return lambda Ns: opt(plus(x))(Ns)


def plus(x): return lambda Ns: genseq(x, star(x), Ns, startx=1)


def oneof(chars): return lambda Ns: set(chars) if 1 in Ns else null


def seq(x, y): return lambda Ns: genseq(x, y, Ns)


def opt(x): return alt(epsilon, x)


dot = oneof("?")


epsilon = lit("") # The pattern that matches the empty string


def genseq(x, y, Ns):
    """
    Generate all concatenated sequences of x and y in the range up Ns inclusive
    that are within the range NS.
    """
    Nss = range(max(Ns) + 1)
    return set(m1 + m2
               for m1 in x(Nss)
               for m2 in y(Nss)
               if len(m1 + m2) in Ns)
