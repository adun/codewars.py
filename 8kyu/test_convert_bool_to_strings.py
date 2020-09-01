# Complete the method that takes a boolean value and return a 'Yes' string for true, or a 'No' string for false.


def bool_to_word(bool):
    return 'Yes' if bool else 'No'


def test_bool_to_word():
    assert bool_to_word(True) == 'Yes'
    assert bool_to_word(False) == 'No'
