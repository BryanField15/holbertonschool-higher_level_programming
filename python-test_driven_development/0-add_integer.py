#!/usr/bin/python3
"""
Module containing one function to add two integers
"""


def add_integer(a, b=98):
    """
    Simple function to add to integers and return an integer
    @param a: integer or float
    @param b: integer or float, default value 98
    @return: integer, the sum of the two parameters
    @raise: TypeError, raised if one/both the parameters is not an int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
