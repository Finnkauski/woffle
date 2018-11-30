#-- Imports ---------------------------------------------------------------------
# base
import random
import re 
# third party
from hypothesis import given
from hypothesis import strategies as st

# project 
from woffle.data.parse import *

#-- Tests -----------------------------------------------------------------------
@given(st.from_regex(re.compile(r"[a-z]+"), fullmatch=True),
       st.from_regex(re.compile(r"[^A-z ]+"), fullmatch=True)
)
def test_letters(just_text, non_letters):
    assert letters(just_text) == just_text
    assert letters(non_letters) == ''
    assert letters(r'*&^%$#@!foo_\{}[]\};+<>\.bar') == 'foobar'

def test_spaces():
    assert spaces('\t'*10) == ' '
    assert spaces(' '*2) == ' '

@given(st.from_regex(re.compile(r"\s[a-z]\s"), fullmatch=True), st.from_regex(re.compile(r"\s?[a-z]{3,}\s?"), fullmatch=True))
def test_singles(char, word):
    assert singles(char) == ''
    assert singles(word) == word

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
