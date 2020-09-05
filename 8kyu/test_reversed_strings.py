# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'


def solution(str):
    return str[::-1]


def test_solution():
    assert solution('world') == 'dlrow'
    assert solution('hello') == 'olleh'
    assert solution('') == ''
    assert solution('h') == 'h'
