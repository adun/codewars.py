# Write a function to convert a name into initials. This kata strictly takes two
# words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
#   Sam Harris => S.H
#   Patrick Feeney => P.F


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


def test_abbrevName():
    assert abbrevName('Sam Harris') == 'S.H'
    assert abbrevName('Patrick Feenan') == 'P.F'
    assert abbrevName('Evan Cole') == 'E.C'
    assert abbrevName('P Favuzzi') == 'P.F'
    assert abbrevName('David Mendieta') == 'D.M'
