from math import factorial
from collections import defaultdict
from random import randrange


def shuffle(deck):
    "Knuth's Algorithm P"
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, randrange(i, N))


def shuffle1(deck):
    "Teacher's algorithm"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def shuffle2(deck):
    "A modification of the teacher's algorithm"
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = randrange(N), randrange(N)
        swapped[i] = True
        swap(deck, i, j)


def shuffle3(deck):
    "An easier modification of the teacher's algorithm"
    N = len(deck)
    for i in range(N):
        swap(deck, i, randrange(N))


def swap(deck, i, j):
    "Swap elements i and j of a collection"
    # print(f"Swap {i} and {j}")
    deck[i], deck[j] = deck[j], deck[i]


def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1

    e = n*1./factorial(len(deck)) ## expected count
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)

    name = shuffler.__name__
    print("{0}({1}) {2}".format(name, deck, ('ok' if ok else '*** BAD ***')))
    print("     ")
    for item, count in sorted(counts.items()):
        print(f"{item}: {count}")
    print()


def test_shufflers(shufflers=[shuffle, shuffle1, shuffle2, shuffle3], decks=['abc', 'ab']):
    for deck in decks:
        print()
        for f in shufflers:
            test_shuffler(f, deck)


test_shufflers()
