import pytest


from subpalindrome import longest_subpalindrome_slice

def test_longest_subpalindrome_slice_for_palindromes():
    L = longest_subpalindrome_slice

    assert L('racecar') == (0, 7)
    assert L('ab') is None
    assert L('Racecar') == (0, 7)
    assert L('') == (0, 0)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
