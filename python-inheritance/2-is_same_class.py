#!/usr/bin/python3
"""Module containing a single function"""


def is_same_class(obj, a_class):
    """Function that checks an instnace of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False
