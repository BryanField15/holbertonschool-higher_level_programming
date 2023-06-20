#!/usr/bin/python3
"""Module containing a single function"""


def inherits_from(obj, a_class):
    """Function to check if obj is an instance of a class that
    inherited (directly or indirectly) from the specified class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
