# My initial solution to generate the sequence: 0, 1, -1, 2, -2...
def all_ints():
    i = 0
    while True:
        if i == 0:
            yield i
            i += 1
        elif i > 0:
            yield i
            i = -i
        elif i < 0:
            yield i
            i = -i + 1


def all_ints_refactored():
    i = 0
    yield i

    while True:
        i += 1
        yield i
        yield -i
