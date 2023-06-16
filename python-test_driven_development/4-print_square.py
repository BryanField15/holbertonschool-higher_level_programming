#!/usr/bin/python3
"""
Module containing function to print a square
"""


def print_square(size):
    """
    Function that  prints a square of 3 with side length size
    Args:
        size: side length of the square
    Return:
        Prints to terminal a sqaure of #'s of side lenght size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
