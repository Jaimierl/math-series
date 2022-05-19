from series.series import fibonacci 
from series.series import lucas
from series.series import sum_series

# To make testing run remember you need to start up your virtual environment and pip install pytest into your virtual environment.

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

def test_sum_series_fibonacci():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_series_lucas():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected

def test_sum_series_negative():
    actual = sum_series(5, -2, 1)
    expected = ("Negative numbers are not supported")
    assert actual == expected
   
def test_sum_series_countdown():
    actual = sum_series(2, 3, 4)
    expected = 7
    assert actual == expected
