null = frozenset([])


def lit(s): return lambda Ns: set([s]) if len(s) in Ns else null


def alt(x, y): return lambda Ns: x(Ns) | y(Ns)


def oneof(chars): return lambda Ns: set(chars) if 1 in Ns else null
