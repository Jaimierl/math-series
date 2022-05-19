from series.series import fibonacci 
from series.series import lucas

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_negative():
    actual = fibonacci(-27)
    expected = ("Negative numbers are not supported")
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_negative():
    actual = lucas(-3)
    expected = ("Negative numbers are not supported")
    assert  actual == expected

# To make testing run remember you need to start up your virtual environment and pip install pytest into your virtual environment.