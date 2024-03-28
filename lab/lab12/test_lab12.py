import pytest
import math
from lab12 import *

# Remember to import from the lab12 file and pytest

# Write your test code here for Q1 and Q2

def test_product():
    assert product(3) == 6
    assert product(4) == 24
    with pytest.raises(ValueError):
        product(-1)

def test_summation():
    assert summation(3) == 6
    assert summation(4) == 10
    with pytest.raises(ValueError):
        summation(-1)

def test_accumulate():
    assert accumulate(add, 0, 3) == 6
    assert accumulate(mul, 2, 4) == 48
    with pytest.raises(ValueError):
        accumulate(mul, 5, 0)

def test_product_short():
    assert product(3) == 6
    assert product(4) == 24
    with pytest.raises(ValueError):
        product(-1)

def test_summation_short():
    assert summation(3) == 6
    assert summation(4) == 10
    with pytest.raises(ValueError):
        summation(-1)

# Q3
#####################################

def test_square():
    """Write your code here"""
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4


def test_sqrt():
    """Write your code here"""
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    for i in range(0,20,3):
        assert pytest.approx(sqrt(i)) == pytest.approx(math.sqrt(i))

def test_mean():
    """Write your code here"""
    assert mean([1,1,1,3,4]) == 2
    assert mean([1,2,3]) == 2
    assert mean([0,0,0,0,0]) == 0
    assert mean([.25,.25,.25,.25]) == pytest.approx(0.25)

def test_median():
    """Write your code here"""
    assert median([1,2,3,4,5]) == 3
    assert median([1,2,3]) == 2
    assert median([1,2,3,4,5,6]) == 3.5
    assert median([5,6,7,8,9,10]) == 7.5


def test_mode():
    """Write your code here"""
    assert mode([1,2,1,1]) == 1
    assert mode([1,1,2,2]) == 1
    assert mode([1,2,2,1]) == 2
    assert mode([6,6,7,7,8,8,8]) == 8


def test_std_dev():
    """Write your code here"""
    assert std_dev([10, 12, 23, 23, 16, 23, 21, 16]) == pytest.approx(4.8989794855664)
    assert std_dev([1, 2, 3, 4, 5]) == pytest.approx(1.4142135623731)
    assert std_dev([1,1,1,1,1]) == 0
    with pytest.raises(AssertionError):
        std_dev(1)
    with pytest.raises(AssertionError):
        std_dev([])

def test_stat_analysis():
    """Write your code here"""

# OPTIONAL
#####################################

def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
