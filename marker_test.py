import pytest
"""
This file is to run multiple tests with the help of markers
Command: pytest -m <marker> -v
example: pytest -m one_two -v  --->> Here 'one_two' is marker name , all the tests case will run 
which is coming under marker named 'one_two'
"""
@pytest.mark.one_two
def test_method1():
    x=6
    y=9
    assert x==y
@pytest.mark.one_two
def test_method2():
    a=10
    b=20
    assert a+10==b

@pytest.mark.three_four
def test_method3():
    a=9
    b=2
    assert a%2==0
@pytest.mark.three_four
def test_method4():
    a=234
    b=2
    assert a%2!=0

