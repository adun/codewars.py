# Given an array of integers your solution should find the smallest integer.
# For example:
#     Given [34, 15, 88, 2] your solution will return 2
#     Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.


def findSmallestInt(arr):
    return min(arr)


def test_findSmallestInt():
    assert findSmallestInt([78, 56, 232, 12, 11, 43]) == 11
    assert findSmallestInt([78, 56, -2, 12, 8, -33]) == -33
    assert findSmallestInt([0, 1-2**64, 2**64]) == 1-2**64
    assert findSmallestInt([-133,-5666,-89,-12341,-321423, 2**64]) == -321423
    assert findSmallestInt([0, 2**64, -1-2**64, 2**64, 2**64]) == -1-2**64
    assert findSmallestInt([1,2,3,4,5,6,7,8,9,10]) == 1
    assert findSmallestInt([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]) == -10
    assert findSmallestInt([-78,56,232,12,8]) == -78
    assert findSmallestInt([78,56,-2,12,-8]) == -8
