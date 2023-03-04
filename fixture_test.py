import pytest

"""
This file is to implement 'fixture' in test.
Fixtures are used to feed some data to the tests such as database connection,URLs to test 
and some sort of input data.
command : pytest -k <fixture_> -v
"""

@pytest.fixture
def input_value():
    input=39
    return input

def test_div_by_3(input_value):
    assert input_value%3==0

def test_div_by_6(input_value):
    assert input_value%6==0