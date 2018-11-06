null = frozenset()


def lit(x): return lambda text: set([text[len(x):]]) if text.startswith(x) else null


def seq(x, y): return lambda text: set().union(*map(y, x(text)))
