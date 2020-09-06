# This is the first step to understanding FizzBuzz.
# Your inputs: a positive integer, n, greater than or equal to one. n is provided,
# you have NO CONTROL over its value.
# Your expected output is an array of positive integers from 1 to n (inclusive).
# Your job is to write an algorithm that gets you from the input to the output.


def pre_fizz(n):
    return list(range(1, n+1))


def test_pre_fizz():
    assert pre_fizz(1) == [1]
    assert pre_fizz(2) == [1,2]
    assert pre_fizz(3) == [1,2,3]
    assert pre_fizz(4) == [1,2,3,4]
    assert pre_fizz(5) == [1,2,3,4,5]
