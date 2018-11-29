import pytest


from json_parser import json_parse

def test_json_parse():
    # assert json_parse('1') == (['value', ['number', '1']], '')
    assert json_parse('["testing", 1, 2, 3]') == (
                       ['value', ['array', '[', ['elements', ['value',
                       ['string', '"testing"']], ',', ['elements', ['value', ['number',
                       ['int', '1']]], ',', ['elements', ['value', ['number',
                       ['int', '2']]], ',', ['elements', ['value', ['number',
                       ['int', '3']]]]]]], ']']], '')

    # assert json_parse('-123.456e+789') == (
    #                    ['value', ['number', ['int', '-123'], ['frac', '.456'], ['exp', 'e+789']]], '')
    #
    # assert json_parse('{"age": 21, "state":"CO","occupation":"rides the rodeo"}') == (
    #                   ['value', ['object', '{', ['members', ['pair', ['string', '"age"'], 
    #                    ':', ['value', ['number', ['int', '21']]]], ',', ['members',
    #                   ['pair', ['string', '"state"'], ':', ['value', ['string', '"CO"']]],
    #                   ',', ['members', ['pair', ['string', '"occupation"'], ':',
    #                   ['value', ['string', '"rides the rodeo"']]]]]], '}']], '')
