def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1


def find_solution_bounds(f, y):
    """
    Find lower and upper bounds such that f(lower) <= y <= f(upper).
    Keep doubling x until f(x) >= y; that's upper; and lower will be either the
    previous upper or 0.
    """
    lower_bound, upper_bound = 0, 1

    while f(upper_bound) < y:
        lower_bound = upper_bound
        upper_bound *= 2

    return lower_bound, upper_bound


def binary_search(lower, upper, f, y, delta):
    """
    Given f(lower) <= y <= f(upper), return x such that f(x) is within delta of
    y.
    """
    while lower <= upper:
        guess = (upper + lower) / 2
        result = f(guess)

        if result < y:
            lower = guess + delta
        elif result > y:
            upper = guess - delta
        else:
            return guess

    return upper if (f(upper)-y < f(lower)+y) else lower


def inverse(f):
    """
    Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta.
    """
    def f_1(y, delta=1/1024):
        lower, upper = find_solution_bounds(f, y)
        return binary_search(lower, upper, f, y, delta)

    return f_1
