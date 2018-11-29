def search(pattern, text):
    """
    Return True if pattern appears anywhere in text.
    """
    # If the pattern needs to start at the beginning, truncate the ^ and send to
    # match since match matches the pattern from the beginning of the text.
    if pattern.startswith("^"):
        return match(pattern[1:], text)

    # Otherwise, match any number of characters before the pattern when sending
    # to match
    return match('.*' + pattern, text)


def match(pattern, text):
    """
    Return True if pattern appears at the start of the text.
    """

    # Guard clause: Every string has at least an empty string, so this pattern will match all
    # strings.
    if pattern == "":
        return True
    # Guard clause: This pattern will only match if the text is the empty string.
    if pattern == "$":
        return text == ""

    # Now we need to deal with the special characters * and ?
    if len(pattern) > 1 and pattern[1] in "*?":
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == "*":
            return match_star(p, pat, text)
        elif op == "?":
            if match1(p, text) and match(pat, text[1:]):
                return True

            return match(pat, text)

    # If the text doesn't match a special character, we'll recursively check if
    # the first character matches the first character of the text
    return match1(pattern[0], text) and match(pattern[1:], text[1:])


def match1(p, text):
    """
    Return True if first character of text matches pattern character p.
    """
    if not text: return False
    return p == "." or p == text[0]


def match_star(p, pattern, text):
    """
    Return True if any number of char p, followed by pattern, matches text.
    """
    return (match(pattern, text) or
            (match1(p, text) and
             match_star(p, pattern, text[1:])))
