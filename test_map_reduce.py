from map_reduce import *


def test_sum_ints():
    assert sum_ints(0, 500) == 125250


def test_sum_cubes():
    assert sum_cubes(0, 50) == 1625625


def test_sum_fact():
    assert sum_fact(0, 5) == 154


def test_fact():
    assert fact(5) == 120


def test_sum_ints_perf():
    assert sum_ints(0, 50000000) == 1250000025 * 1000000
