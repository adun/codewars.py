# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    return sum(n for n in arr if n > 0)


def test_positive_sum():
    assert positive_sum([1,2,3,4,5]) == 15
    assert positive_sum([1,-2,3,4,5]) == 13
    assert positive_sum([-1,2,3,4,-5]) == 9

def test_positive_sum_returns_0_when_array_is_empty():
    assert positive_sum([]) == 0

def test_positive_sum_returns_0_when_all_elements_are_negative():
    assert positive_sum([-1,-2,-3,-4,-5]) == 0
