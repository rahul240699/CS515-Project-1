import unittest

print("Hello World!")

#tests with pytest.py

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 1