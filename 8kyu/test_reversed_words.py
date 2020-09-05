# Complete the solution so that it reverses all of the words within the string passed in.
# Example:
#   reverseWords("The greatest victory is that which requires no battle")
#   // should return "battle no requires which that is victory greatest The"


def reverseWords(str):
    return " ".join(str.split(" ")[::-1])


def test_reverseWords():
    assert reverseWords("hello world!") == "world! hello"
    assert reverseWords("yoda doesn't speak like this" ) ==  "this like speak doesn't yoda"
    assert reverseWords("foobar"                       ) ==  "foobar"
    assert reverseWords("kata editor"                  ) ==  "editor kata"
    assert reverseWords("row row row your boat"        ) ==  "boat your row row row"
