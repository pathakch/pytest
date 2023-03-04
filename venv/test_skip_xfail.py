import pytest

"""

"""

@pytest.mark.xfail
def test_method1():
    a=10
    b=20
    c=50
    assert a*b==c

@pytest.mark.skip
def test_method2():
    a=200
    assert a%2!=0

def test_method3():
    a=20
    b=40
    assert a*b==800

def test_method4():
    assert 10%5!=0