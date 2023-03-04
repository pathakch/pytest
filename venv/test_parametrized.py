import pytest


@pytest.mark.parametrize("x,y,z",[(10,20,200),(20,40,200)])  # x=10,y=20,z=200 and x=20,y=40,z=200
def test_method(x,y,z):
    assert x*y==z

@pytest.mark.parametrize('num,output',[(1,20),(3,37),(4,40),(5,50)])
def test_multiplication(num,output):
    assert 10*num==output





