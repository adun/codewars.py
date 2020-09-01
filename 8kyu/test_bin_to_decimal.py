# Complete the function which converts a binary number (given as a string) to a decimal number.


def bin_to_decimal(inp):
    return int(inp, 2)


def test_bin_to_decimal():
    assert bin_to_decimal('1') == 1
    assert bin_to_decimal('0') == 0
    assert bin_to_decimal('1001001') == 73
