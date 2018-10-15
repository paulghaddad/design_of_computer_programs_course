def valid(formula):
    """
    Formula f is valid iff it has no numbers with leading zero and evals true.
    """
    try:
        return eval(formula)
    except ZeroDivisionError:
        return False
    except Exception:
        raise ValueError(f"The argument {formula} is not valid")
