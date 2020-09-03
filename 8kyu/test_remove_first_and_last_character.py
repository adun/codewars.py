# It's pretty straightforward. Your goal is to create a function that removes the
# first and last characters of a string. You're given one parameter, the original
# string. You don't have to worry with strings with less than two characters.


def remove_char(s):
    return s[1 : -1]


def test_remove_char():
    assert remove_char('eloquent') == 'loquen'
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''
    assert remove_char('ooopsss') == 'oopss'
