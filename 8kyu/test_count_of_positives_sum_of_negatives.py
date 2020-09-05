# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and
# the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.
# Example
#   For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
#   you should return [10, -65].


def count_positives_sum_negatives(arr):
    return [sum(x>0 for x in arr), sum(y for y in arr if y < 0)] if arr else []


def test_count_positives_sum_negatives():
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10,-65]
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8,-50]
    assert count_positives_sum_negatives([1]) == [1,0]
    assert count_positives_sum_negatives([-1]) == [0,-1]
    assert count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]) == [0,0]
    assert count_positives_sum_negatives([]) == []
