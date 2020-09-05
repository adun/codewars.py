# The function is not returning the correct values. Can you figure out why?
# get_planet_name(3) # should return 'Earth'


def get_planet_name(id):
    return {
        1: 'Mercury',
        2: 'Venus',
        3: 'Earth',
        4: 'Mars',
        5: 'Jupiter',
        6: 'Saturn',
        7: 'Uranus',
        8: 'Neptune',
    }.get(id, None)


def test_():
    assert get_planet_name(2) == 'Venus'
    assert get_planet_name(5) == 'Jupiter'
    assert get_planet_name(3) == 'Earth'
    assert get_planet_name(4) == 'Mars'
    assert get_planet_name(8) == 'Neptune'
    assert get_planet_name(1) == 'Mercury'
