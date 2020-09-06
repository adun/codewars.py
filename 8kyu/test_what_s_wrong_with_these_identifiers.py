# An identifier is simply a name...
# Can you amend this object so that its properties comprise only vaild identifiers?


Person = {
    '1stname': 'John',
    'second-name': 'Doe',
    'email@ddress': 'john.doe@email.com',
    'male.female': 'M'
}



def test_should_be_defined():
    assert Person, 'Person is not defined'


def test_should_have_at_least_4_properties():
    assert len(Person.keys()) == 4, 'Person does not have 4 properties'
