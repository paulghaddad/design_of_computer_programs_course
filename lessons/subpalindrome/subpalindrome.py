def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)
    normalized_text = text.lower()

    longest_subpalindromes = []
    left_edge, right_edge = 0, 2*len(normalized_text) - 1

    longest_subpalindromes = [_grow(normalized_text, i, i+i%2) for i in range(right_edge)]

    return max(longest_subpalindromes, key=_length)


def _length(subpalindrome):
    "Return the difference in a two element tuple."
    return subpalindrome[1] - subpalindrome[0]


def _grow(text, start, end):
    while (start >= 0 and end < 2*len(text) - 1 and text[(start//2)] == text[(end//2)]):
        start -= 2; end += 2

    return (start//2+1, end//2)


def _palindrome(string):
    "Return a Boolean indicating whether the string is a palindrome."
    reversed_string = ''
    for letter in reversed(string):
        reversed_string += letter

    return string == reversed_string
