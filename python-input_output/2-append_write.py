#!/usr/bin/python3
"""Module with one function to append string"""


def append_write(filename="", text=""):
    """Function appends string to end of a text file
        returns the number of characters added"""
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
