import itertools


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
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory) #6
            for (Englishman, Spaniard, Ukranian, Japanese, Norweigian) in orderings
            if Englishman is red  # 2
            if Norweigian is first #10
            if nextto(Norweigian, blue) #15
            for (coffee, tea, milk, oj, WATER) in orderings
            if coffee is green #4
            if Ukranian is tea #5
            if milk is middle #9
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Kools is yellow #8
            if LuckyStrike is oj #13
            if Japanese is Parliaments #14
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard is dog #3
            if OldGold is snails #7
            if nextto(Chesterfields, fox) #11
            if nextto(Kools, horse) #12
            )

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.perf_counter()
    result = fn(*args)
    t1 = time.perf_counter()
    return t1-t0, result


def timedcalls(n, fn, *args):
    "Call function n times with args; return the min, avg and max time."
    times = [timedcall(fn, *args)[0] for _ in range(n)]
    return min(times), average(times), max(times)


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))


print(timedcalls(1000, zebra_puzzle))
