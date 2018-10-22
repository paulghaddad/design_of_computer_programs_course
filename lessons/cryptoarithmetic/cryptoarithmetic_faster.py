import itertools
import re


def compile_word(word):
    """
    Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'
    """
    if str.isupper(word):
        letters = list(word)

        terms = [f"{10**digit}*{letter}" for digit, letter in enumerate(reversed(letters))]

        return f"({' + '.join(terms)})"
    else:
        return word


def solve(formula):
    """
    Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula.
    """
    f, letters = compile_formula(formula)

    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """
    Compile formula into a function. Also return letters found, as a str, in the
    same order as params of function. For example: `YOU == ME**2' returns
    (lambda Y, M, E, U, O: (U+10*M)**2), 'YMEUO'

    The first digit of a multi-digit number can't be 0. So if YOU is a word in
    the formula, and the function is called with Y equal to 0, the function should
    return False.
    """
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    leading_digits = set(re.findall(r"([A-Z])[A-Z]+", formula))
    body = ''.join(tokens)

    if leading_digits:
        leading_digits_list = f"[{', '.join(leading_digits)}]"
        body += f" and 0 not in {leading_digits_list}"

    f = f"lambda {params}: {body}"
    if verbose: print(f)
    return eval(f), letters
