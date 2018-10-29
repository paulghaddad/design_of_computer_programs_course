import pytest


from subpalindrome import longest_subpalindrome_slice

def test_longest_subpalindrome_slice_for_palindromes():
    L = longest_subpalindrome_slice

    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('') == (0, 0)
    assert L('xxxxx') == (0, 5)


def test_longest_subpalindrome_slice_for_subpalindromes():
    L = longest_subpalindrome_slice

    assert L('aba') == (0, 3)
    assert L('abba') == (0, 4)
    assert L('RacecarX') == (0, 7)
    assert L('xxxabc') == (0, 3)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L('Race carr') == (7, 9)
    assert L('Race crrr') == (6, 9)
    assert L('something rac e car going') == (8,21)
