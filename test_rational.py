from rational import *

def test_rational_add():
    a = Rational(2, 3)
    b = Rational(3, 5)
    actual = a + b
    expected = Rational(19, 15)
    actual == expected

