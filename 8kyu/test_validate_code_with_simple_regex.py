# Basic regex tasks. Write a function that takes in a numeric code of any length.
# The function should check if the code begins with 1, 2, or 3 and return true if so.
# Return false otherwise.
# You can assume the input will always be a number.


import re


def validate_code(code):
    return bool(re.match('^[123]',str(code)))


def test_validate_code():
    assert validate_code(123) == True
    assert validate_code(248) == True
    assert validate_code(8) == False
    assert validate_code(321) == True
    assert validate_code(9453) == False
