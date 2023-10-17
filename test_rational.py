from rational import *

def test_rational_add():
    a = Rational(2, 3)
    b = Rational(3, 5)
    actual = a + b
    expected = Rational(19, 15)
    actual == expected

def test_rational_simplifies():
    a = Rational(1, 2)
    actual = a + a
    expected = Rational(1, 1)
    actual == expected