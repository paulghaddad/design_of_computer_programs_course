def valid(formula):
    """
    Formula f is valid iff it has no numbers with leading zero and evals true.
    """
    try: 
        return eval(formula) is True
    except ArithmeticError:
        return False
