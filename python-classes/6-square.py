#!/usr/bin/python3


'''Define the class called Square'''


class Square:
    '''A class that defines a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize Square instance with size amd position'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieve the size of the square'''
        return self.__size

    @property
    def position(self):
        '''Retrieve the position of the square'''
        return self.__position

    @size.setter
    def size(self, value):
        '''Set the size of the square, raise exceptions for invalid values'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        '''Positions the square'''
        if (not isinstance(value, tuple) or len(value) != 2 or
            any(isinstance(i, int) and i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the current square area'''
        return self.__size ** 2

    def my_print(self):
        '''prints the square using the character #'''
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
