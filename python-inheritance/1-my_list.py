#!/usr/bin/python3
"""Module for MyList subclass"""


class MyList(list):
    """Class that inherits from class list"""
    def print_sorted(self):
        """Method prints the list, sorted ascedning"""
        print(sorted(self))
