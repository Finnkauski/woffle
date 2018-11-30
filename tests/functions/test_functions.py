
#-- Imports ---------------------------------------------------------------------
# base
import functools

# third party
from woffle.functions.compose import *

from hypothesis import given
from hypothesis import strategies as st

#-- Fixtures & Definitions ------------------------------------------------------

#-- Tests -----------------------------------------------------------------------
def test_id():
    assert id(1) is 1

@given(st.lists(st.integers()))
def test_basic_composition(integers):
    comp = compose(str, sum, functools.partial(map, int))
    assert callable(comp)  
    assert comp(integers) == str(sum(map(int,integers)))
