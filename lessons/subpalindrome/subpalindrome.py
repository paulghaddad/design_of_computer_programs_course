def longest_subpalindrome_slice(string):
    if _palindrome(string.lower()):
        return (0, len(string))
    else:
        return longest_subpalindrome_slice(string[:-1])


def _palindrome(string):
    reversed_string = ''
    for letter in reversed(string):
        reversed_string += letter

    return string == reversed_string
