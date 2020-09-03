# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?
# Example:
#   make_negative(1);  # return -1
#   make_negative(-5); # return -5
#   make_negative(0);  # return 0
# Notes:
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.


def make_negative( number ):
    return -abs(number)


def test_make_negative():
    assert make_negative(42) == -42
    assert make_negative(-9) == -9
    assert make_negative(0) == 0
    assert make_negative(1) == -1
    assert make_negative(-1) == -1
