import re


def valid(formula):
    """
    Formula f is valid if it has no numbers with leading zero and evals true.
    """
    try: 
        return not re.search(r"\b0[0-9]", formula) and eval(formula) is True
    except ArithmeticError:
        return False
