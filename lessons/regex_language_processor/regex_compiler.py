null = frozenset()


def lit(x): return lambda text: set([text[len(x):]]) if text.startswith(x) else null


def seq(x, y): return lambda text: set().union(*map(y, x(text)))


def alt(x, y): return lambda text: x(text) | y(text)


def oneof(chars): return lambda text: set([text[1:]]) if (text and text[0] in chars) else null


dot = lambda text: set([text[:1]]) if text else null


eol = lambda text: set(['']) if text == '' else null
