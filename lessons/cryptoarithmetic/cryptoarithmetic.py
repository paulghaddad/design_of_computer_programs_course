import itertools
import re


def solve(formula):
    """
    Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or
    None.
    """
    # Find all combinations for the given formula
    formula_combinations = fill_in(formula)

    # Check each with valid and return the first one
    return next(f for f in formula_combinations if valid(f))

    # If none are found, return None


def solve_norvig(formula):
    """
    Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or
    None.
    """
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(formula):
    """
    Formula f is valid if it has no numbers with leading zero and evals true.
    """
    try: 
        return not re.search(r"\b0[0-9]", formula) and eval(formula) is True
    except ArithmeticError:
        return False
