from test_black import *
import math


def unreachable_return(value=0):
    """This function needs a non constant condition"""
    condition = 1
    if True:
        return True
    return False


def sumIntegers(value):
    """This function returns the sum of 2 integers"""
    a, b, c = 5, 3, value
    return simple_sum(a, b)


def math_sqrt(value) -> str:
    return math.sqrt(value)


def type_sum(x: None, y: dict):
    return x + y
