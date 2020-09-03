# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array
# (true means present).
# For example,
#   [True,  True,  True,  False,
#    True,  True,  True,  True ,
#    True,  False, True,  False,
#    True,  False, False, True ,
#    True,  True,  True,  True ,
#    False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)


def test_count_sheeps1():
    array1 = [True,  True,  True,  False,
        True,  True,  True,  True ,
        True,  False, True,  False,
        True,  False, False, True ,
        True,  True,  True,  True ,
        False, False, True,  True ]
    assert count_sheeps(array1) == 17, f"There are 17 sheeps in total, not {count_sheeps(array1)}"


    array2 = []
    array2.extend([True] * 500)
    array2.extend([None] * 5)
    array2.extend([False] * 100)
    assert count_sheeps(array2) == 500, f"There are 500 sheeps in total, not {count_sheeps(array2)}"


def test_count_sheeps3():
    array3 = []
    assert count_sheeps(array3) == 0, f"There are no sheeps at all, you counted {count_sheeps(array3)}"
