import time

from cryptoarithmetic import solve


examples = """TWO + TWO == FOUR
A**2 + B**2  == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANETS])""".splitlines()


def timedcall(fn, *args):
    t0 = time.perf_counter()
    result = fn(*args)
    t1 = time.perf_counter()
    return t1-t0, result


def test():
    t0 = time.clock()
    for example in examples:
        process_time, result = timedcall(solve, example)
        print()
        print(f"{13*' '} {example}")
        print(f"{process_time} sec:   {result}")
        print(f"{time.clock() - t0} total time.")


test()
