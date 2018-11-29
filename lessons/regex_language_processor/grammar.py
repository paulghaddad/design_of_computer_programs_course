import re
from tools import memo


def grammar(description, whitespace=r'\s*'):
    """
    Convert a description to a grammar. Each line is a rule for a non-terminal
    symbol; it looks like this:
        Symbol => A1 A2 ... | B1 B2 ... | C1 C2 ...
        where the right-hand side is one or more alternatives, separated by the
        '|' sign. Each alternative is a sequence of atoms, separated by spaces.
        An atom is either a symbol on some left-hand side, or it is a regular
        expression that will be passed to re.match to match a token. Notation
        for *, +, or ? not allowed in a rule alternative (but ok within a
        token). Use '\' to continue long lines. You must include spaces or tabs
        around '=>' and '|'. That's within the grammar description itself. The
        grammar that gets defined allows whitespace between tokens by default,
        specify '' as the second argument to grammar() to disallow this (or
        supply any regular expression to describe allowable whitespace between
        tokens).
    """
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G


def split(text, sep=None, maxsplit=-1):
    "Like str.split applied to text, but strips whitespace from each piece."
    return [t.strip() for t in text.strip().split(sep, maxsplit) if t]

G = grammar(r"""
Exp     => Term [+-] Exp | Term
Term    => Factor [*/] Term | Factor
Factor  => Funcall | Var | Num | [(] Exp [)]
Funcall => Var [(] Exps [)]
Exps    => Exp [,] Exps | Exp
Var     => [a-zA-Z_]\w*
Num     => [-+]?[0-9]+([.][0-9]*)?
""")


def verify(G):
    """Verify the grammar is correct."""
    lhstokens = set(G) - set([' '])
    rhstokens = set(t for alts in G.values() for alt in alts for t in alt)
    def show(title, tokens): print(title, '=', ' '.join(sorted(tokens)))
    show('Non-Terms', G)
    show('Terminals', rhstokens - lhstokens)
    show('Suspects', [t for t in (rhstokens -lhstokens) if t.isalnum()])
    show('Orphans', lhstokens - rhstokens)


def parse(start_symbol, text, grammar):
    """
    Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string; failure if remainder is None. This is a deterministic PEG parser, so
    rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'.
    Also, no left recursion allowed: don't do 'E => E op T'
    """

    # First define the tokenizer. Two jobs, handle whitespace before the token.
    # Then build up a regular expression that will parse the appropriate amount
    # of whitespace (some, all, none). And then parse off whatever was defined
    # by the atom we look at next.
    tokenizer  = grammar[' '] + '(%s)'

    # We go through a sequence of atoms. We'll try to parse an atom one at a
    # time, appending the tree to the result each time. Note that we update the
    # `text` variable each time through the loop as the remainder of the
    # previous atom.
    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    # Handles two cases. If the atom is in the grammar, we map it into a tuple
    # of alternatives. For each alternative, we try to parse and if we have a
    # successful match, we return a built-up tree structure and the remainder.
    # If we exhaust the alternatives and don't match anything, we return Fail.
    # Otherwise, if the atom is not in the grammar, then it must be a regular
    # expression. We take the tokenizer and insert the atom, matching it against
    # the text. If there's no match, we Fail, otherwise, we pull out the
    # matching part, and take the rest of the text after the match, returning a
    # tuple of these two items. This is the only part of the code that advances
    # the text.
    @memo
    def parse_atom(atom, text):
        if atom in grammar: # Non-terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem
            return Fail

        else: # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])

    # Body of parse
    return parse_atom(start_symbol, text)

Fail = (None, None)
