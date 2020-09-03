# Add the value "codewars" to the websites array.
# After your code executes the websites array should == ["codewars"]
# The websites array has already been defined for you using the following code:
# websites = []

websites = []
websites.append("codewars")


def test():
    assert websites == websites, "You assigned a new array to the websites variable. You should instead alter the existing reference."
    assert len(websites) > 0, 'The array is still empty'
    assert len(websites) == 1, 'The array contains too many values'
    assert websites[0] == 'codewars', 'The array does not contain the correct value "codewars"'
