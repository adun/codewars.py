# Remove a exclamation mark from the end of string. For a beginner kata, you can assume
# that the input data is always a string, no need to verify it.
# Examples
#   remove("Hi!") === "Hi"
#   remove("Hi!!!") === "Hi!!"
#   remove("!Hi") === "!Hi"
#   remove("!Hi!") === "!Hi"
#   remove("Hi! Hi!") === "Hi! Hi"
#   remove("Hi") === "Hi"


def remove(s):
    return s[:-1] if s.endswith('!') else s


def test_remove():
    assert remove("Hi!") == "Hi"
    assert remove("Hi!!!") == "Hi!!"
    assert remove("!Hi") == "!Hi"
    assert remove("!Hi!") == "!Hi"
    assert remove("Hi! Hi!") == "Hi! Hi"
    assert remove("Hi") == "Hi"
