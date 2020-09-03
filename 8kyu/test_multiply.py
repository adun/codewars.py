# This code does not execute properly. Try to figure out why.


def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(1,1) == 1
    assert multiply(2,1) == 2
    assert multiply(2,2) == 4
    assert multiply(3,5) == 15
    assert multiply(1.5,2.5) == 3.75
    assert multiply(0,5) == 0
    assert multiply(0,0) == 0
