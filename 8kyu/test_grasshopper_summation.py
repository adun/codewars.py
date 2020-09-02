# Summation
# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
# For example:
#   summation(2) -> 3
#   1 + 2
#   summation(8) -> 36
#   1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    return (1+num) * num / 2


def test_summation():
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791
