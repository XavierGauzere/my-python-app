# test_main.py
from main import add, essai

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_essai():
    assert essai(2) == 4
    assert essai(3) == 9
    assert essai(0) == 0