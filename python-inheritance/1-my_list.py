#!/usr/bin/python3
"""Simple sort function"""


class MyList(list):
"""Class that inherits from class list"""
    def print_sorted(self):
        """Function prints the list, sorted ascedning"""
        print(sorted(self))
