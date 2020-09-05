# Complete the square sum function so that it squares each number passed into
# it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


def test_square_sum():
    assert square_sum([1,2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50
    assert square_sum([]) == 0
    assert square_sum([-1,-2]) == 5
    assert square_sum([-1,0,1]) == 2
