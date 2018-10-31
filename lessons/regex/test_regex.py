import pytest


from regex import search, match

def test_search():
    assert search("baa*!", "Sheep said baaa!") is True
    assert search("baa*!", "Sheep said baaa humbug") is False


def test_match():
    assert match("baa*!", "Sheep said baaa!") is False
    assert match("baa*!", "baaa!") is True
