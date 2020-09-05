# Create a function (or write a script in Shell) that takes an integer as an argument
# and returns "Even" for even numbers or "Odd" for odd numbers.


def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'


def test_even_or_odd():
    assert even_or_odd(2) == 'Even'
    assert even_or_odd(1) == 'Odd'
    assert even_or_odd(0) == 'Even'
    assert even_or_odd(1545452) == 'Even'
    assert even_or_odd(7) == 'Odd'
    assert even_or_odd(78) == 'Even'
    assert even_or_odd(17) == 'Odd'
    assert even_or_odd(74156741) == 'Odd'
    assert even_or_odd(100000) == 'Even'
    assert even_or_odd(-123) == 'Odd'
    assert even_or_odd(-456) == 'Even'
