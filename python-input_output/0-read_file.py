#!/usr/bin/python3
""""""


def read_file(filename=""):
    """Function reads a text file (UTF8), prints to stdout"""
    with open(filename) as f:
        contents = f.read()
    print(contents)
