
#-- Imports ---------------------------------------------------------------------
# base
import functools

# third party
import pytest
from woffle.functions.compose import *

from hypothesis import given
from hypothesis import strategies as st

#-- Fixtures & Definitions ------------------------------------------------------

#-- Tests -----------------------------------------------------------------------
def test_id():
    assert id(1) is 1

@given(st.lists(st.integers()))
def test_basic_composition(integers):
    assert compose(str, sum, functools.partial(map, int))(integers) == str(sum(map(int,integers)))
