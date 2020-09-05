# Jenny has written a function that returns a greeting for a user. However,
# she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
# Can you help her?


def greet(name):
    return f"Hello, {'my love' if name == 'Johnny' else name}!"


def test_should_greet_some_people_normally():
    assert greet('James') == 'Hello, James!'
    assert greet('Jane') == 'Hello, Jane!'
    assert greet('Jim') == 'Hello, Jim!'

def test_should_greet_Johnny_a_little_bit_more_special():
    assert greet('Johnny') == 'Hello, my love!'
