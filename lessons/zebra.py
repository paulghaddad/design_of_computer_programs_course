import itertools
import time


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 = 1"
    return h1 - h2 == 1


def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1"
    return abs(h1 - h2) == 1


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # Constraint 1

    return next((WATER, ZEBRA) 
            for (red, green, ivory, yellow, blue) in c(orderings)
            if imright(green, ivory) #6
            for (Englishman, Spaniard, Ukranian, Japanese, Norweigian) in c(orderings)
            if Englishman is red  # 2
            if Norweigian is first #10
            if nextto(Norweigian, blue) #15
            for (coffee, tea, milk, oj, WATER) in c(orderings)
            if coffee is green #4
            if Ukranian is tea #5
            if milk is middle #9
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
            if Kools is yellow #8
            if LuckyStrike is oj #13
            if Japanese is Parliaments #14
            for (dog, snails, fox, horse, ZEBRA) in c(orderings)
            if Spaniard is dog #3
            if OldGold is snails #7
            if nextto(Chesterfields, fox) #11
            if nextto(Kools, horse) #12
            )


def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print(f"{fn.__name__} got {result} with {c.starts} iters over {c.items} items")


def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.starts is the
    number of sequences started; c.items is the number of items generated."""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item


instrument_fn(zebra_puzzle)
# zebra_puzzle got (1, 5) with 25 iters over 2775 items.


def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.perf_counter()
    result = fn(*args)
    t1 = time.perf_counter()
    return t1-t0, result


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to n seconds if n
    is a float; return the min, average and max time."""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            function_runtime = timedcall(fn, *args)[0]
            times.append(function_runtime)

    return min(times), average(times), max(times)


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))


# print(timedcalls(2.0, zebra_puzzle))
