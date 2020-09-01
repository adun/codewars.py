# Write a comparator for a list of phonetic words for the letters of the greek alphabet.


greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)


def test_greek_comparator():
    assert greek_comparator('alpha', 'beta')  < 0, "result should be negative"
    assert greek_comparator('chi', 'chi') == 0, "result should be zero"
    assert greek_comparator('upsilon', 'rho') > 0, "result should be positive"
