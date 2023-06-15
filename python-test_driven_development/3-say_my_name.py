#!/usr/bin/python3
"""
Module containing one function to concatenate a full name
"""


def say_my_name(first_name, last_name=""):
    """
    Function to concatenate the first and last names

    Args:
        first_name: persons first name
        last_name: persons last name
    Return:
        Prints to terminal "My name is <first name> <last name>"
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print(f"My name is {first_name} {last_name}")
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
