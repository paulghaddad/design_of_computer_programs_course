from functools import update_wrapper


null = frozenset([])


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d


@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f


@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args,  we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)

    return _f


@n_ary
def seq(x, y): return ('seq', x, y)


seq = n_ary(seq)


def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null


def alt(x, y): return lambda Ns: x(Ns) | y(Ns)


def star(x): return lambda Ns: opt(plus(x))(Ns)


# we need to specify startx to avoid infinite recursion
def plus(x): return lambda Ns: genseq(x, star(x), Ns, startx=1)


def oneof(chars): return lambda Ns: set(chars) if 1 in Ns else null


# no need to specify startx because no infinite recursion is possible

def seq(x, y): return lambda Ns: genseq(x, y, Ns)


def opt(x): return alt(epsilon, x)


dot = oneof("?")


epsilon = lit("") # The pattern that matches the empty string


def genseq(x, y, Ns, startx=0):
    """
    Generate all concatenated sequences of x and y in the range up Ns inclusive
    that are within the range NS.

    Tricky part: x+ is defined as: x+ = x x*
    To stop the recursion, the first x must generate at least 1 char,
    and then the recursive x* has that many fewer characters. We use startx=1
    to say that x must match at least 1 character.
    """
    if not Ns:
        return null
    xmatches = x(set(range(startx, max(Ns) + 1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m >= 0)
    ymatches = y(Ns_y)
    return set(m1 + m2
               for m1 in xmatches
               for m2 in ymatches
               if len(m1 + m2) in Ns)
