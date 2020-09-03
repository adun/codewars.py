# This function should return an object, but it's not doing what's intended. What's wrong?


def mystery():
    return {'sanity': 'Hello'}


def test_mystery():
    assert mystery() == {'sanity': 'Hello'}, 'Mystery has not returned to sanity'
