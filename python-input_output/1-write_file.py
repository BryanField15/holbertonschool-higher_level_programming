#!/usr/bin/python3
"""Module with one function that write a string to text file"""


def write_file(filename="", text=""):
    """Writes string to text file (UTF8) returns number of characters written"""
    with open(filename, "w") as f:
        f.write(text)
        return len(filename)
