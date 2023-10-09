from fixpoint import *


def test_fixpoint():
    assert fixed_point(lambda x: 1 + x / 2, 1) == 2


def test_sqrt():
    assert sqrt(9) == 3
