# I would like to be able to pass an array with two elements to my swapValues function
#  to swap the values. However it appears that the values aren't changing.
# Can you figure out what's wrong here?


def swap_values(args):
    args[0], args[1] = args[1], args[0]


def test_swap_values():
    arr = [1, 2]
    swap_values(arr)
    assert arr == [2, 1]
