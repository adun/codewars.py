# Given 2 strings, a and b, return a string of the form short+long+short, with the
# shorter string on the outside and the longer string on the inside. The strings will
# not be the same length, but they may be empty ( length 0 ).
# For example:
#   solution("1", "22") # returns "1221"
#   solution("22", "1") # returns "1221"


def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b


def test_solution():
    assert solution('45', '1') == '1451'
    assert solution('13', '200') == '1320013'
    assert solution('Soon', 'Me') == 'MeSoonMe'
    assert solution('U', 'False') == 'UFalseU'
