#!/usr/bin/python3
"""Module containing a single function"""


def is_kind_of_class(obj, a_class):
    """Function that checks an instnace of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
