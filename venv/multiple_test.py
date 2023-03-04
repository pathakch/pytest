import pytest

""" This file is to execute the test containing a string in its name 
    We can use the following syntax to run this file 
    command : pytest -k <substring> -v 
    example : pytest -k method1 -v
"""

def test_method1():
    x=6
    y=9
    assert x==y

def test_method2():
    a=10
    b=20
    assert a+10==b


def test_method3():
    a=9
    b=2
    assert a%2==0

def test_method4():
    a=234
    b=2
    assert a%2!=0
