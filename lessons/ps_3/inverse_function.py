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

def inverse(f):
    """
    Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta.
    """
    def f_1(y, delta=1/128):
        lower = 0
        upper = y

        while True:
            guess = (upper + lower) / 2
            result = f(guess)

            if abs(result - y) < delta:
                return guess
            if result < y:
                lower = guess
            elif result > y:
                upper = guess

    return f_1
