# Write function avg which calculates average of numbers in given list.


def find_average(array):
    return sum(array) / len(array) if array else 0

def test_find_average():
    assert find_average([1, 2, 3]) == 2
