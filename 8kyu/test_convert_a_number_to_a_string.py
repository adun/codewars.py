# We need a function that can transform a number into a string.

# What ways of achieving this do you know?
# Examples:
#   number_to_string(123) /* returns '123' */
#   number_to_string(999) /* returns '999' */


def number_to_string(num):
    return str(num)


def test_number_to_string():
    assert number_to_string(67) == '67'
    assert number_to_string(79585) == '79585'
    assert number_to_string(79585) != 79585
    assert number_to_string(1+2) == '3'
    assert number_to_string(1-2) == '-1'
