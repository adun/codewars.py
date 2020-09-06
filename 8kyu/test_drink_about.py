# Drink about
#   Kids drink toddy.
#   Teens drink coke.
#   Young adults drink beer.
#   Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:
#   Children under 14 old.
#   Teens under 18 old.
#   Young under 21 old.
#   Adults have 21 or more.
# Examples:
#   people_with_age_drink(13) == "drink toddy"
#   people_with_age_drink(17) == "drink coke"
#   people_with_age_drink(18) == "drink beer"
#   people_with_age_drink(20) == "drink beer"
#   people_with_age_drink(30) == "drink whisky"


def people_with_age_drink(age):
    if age < 14: return 'drink toddy'
    if age < 18: return 'drink coke'
    if age < 21: return 'drink beer'
    return 'drink whisky'


def test_should_return_drink_toddy_when_age_is_less_than_14():
    assert people_with_age_drink(13) == 'drink toddy', "Wrong result for 13"
    assert people_with_age_drink(0) == 'drink toddy', "Wrong result for 0"


def test_should_return_drink_coke_when_age_is_between_14_inclusive_and_18_exclusive():
    assert people_with_age_drink(17) == 'drink coke'
    assert people_with_age_drink(15) == 'drink coke'
    assert people_with_age_drink(14) == 'drink coke'


def test_should_return_drink_beer_when_age_is_between_18_inclusive_and_21_exclusive():
    assert people_with_age_drink(20) == 'drink beer'
    assert people_with_age_drink(18) == 'drink beer'


def test_should_return_drink_whisky_when_age_is_greater_than_or_equal_to_21():
    assert people_with_age_drink(22) == 'drink whisky'
    assert people_with_age_drink(21) == 'drink whisky'
