from MapReduce import *

def test_sumInts():
    assert sumInts(0, 500) == 125250

def test_sumCubes():
    assert sumCubes(0, 50) == 1625625

def test_sumFact():
    assert sumFact(0, 5) == 154

def test_fact():
    assert fact(5) == 120

def test_sumIntsPerfTest():
    assert sumInts(0, 50000000) == 1250000025 * 1000000