#!/usr/bin/python3
"""Module with one function to read a text file"""


def read_file(filename=""):
    """Function reads a text file (UTF8), prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
    print(contents, end="")
