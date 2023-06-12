#!/usr/bin/python3


'''Define the class called Square'''


class Square:
    '''A class that defines a square'''

    def __init__(self, size=0):
        '''Initialize Square instance with size'''
        self.size = size

    @property
    def size(self):
        '''Retrieve the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square, raise exceptions for invalid values'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Return the current square area'''
        return self.__size ** 2
