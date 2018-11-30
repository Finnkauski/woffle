#-- Imports ---------------------------------------------------------------------
# base
import random

# third party
from hypothesis import given
from hypothesis import strategies as st

# project 
from woffle.data.parse import *

#-- Tests -----------------------------------------------------------------------
def test_letters():
    assert letters('foobar') == 'foobar'
    assert letters('foo_bar') == 'foobar'

def test_spaces():
    assert spaces('  ') == ' '

@given(st.characters())
def test_singles(char):
    char_spaces = ' ' + char + ' ' 
    assert singles(char) == ''
    assert singles(char_spaces) == ''

@given(st.text(st.characters(blacklist_characters=['\n'])))
def test_unlines(word):
    position = random.randint(0,len(word))
    test_case = word[:position] + '\n' + word[position:]
    assert unlines(test_case) == word
    assert unlines('\n\n\n\n') == ''

def test_domainbias():
    bias_words = [
        'products',
        'goods'
    ]
    for s in ['test ' + w for w in bias_words]:
        assert domainbias(s) == 'test'
