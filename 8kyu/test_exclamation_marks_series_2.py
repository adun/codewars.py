# Exclamation marks series #2: Remove all exclamation marks from the end of sentence

def remove(s):
    return s.rstrip('!')


def test_remove():
    assert remove("Hi!") == "Hi"
    assert remove("Hi!!!") == "Hi"
    assert remove("!Hi") == "!Hi"
    assert remove("!Hi!") ==  "!Hi"
    assert remove("Hi! Hi!") == "Hi! Hi"
    assert remove("Hi") == "Hi"
