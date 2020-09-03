# Create a function that checks if a number n is divisible by two numbers x AND y.
# All inputs are positive, non-zero digits.
# Examples:
#   1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
#   2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
#   3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
#   4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5


def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0


def test_is_divisible():
    assert is_divisible(3,2,2) == False
    assert is_divisible(3,3,4) == False
    assert is_divisible(12,3,4) == True
    assert is_divisible(8,3,4) == False
    assert is_divisible(48,3,4) == True
    assert is_divisible(100,5,10) == True
    assert is_divisible(100,5,3) == False
    assert is_divisible(4,4,2) == True
    assert is_divisible(5,2,3) == False
    assert is_divisible(17,17,17) == True
    assert is_divisible(17,1,17) == True
