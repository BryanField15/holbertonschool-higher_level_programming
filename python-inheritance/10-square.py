#!/usr/bin/python3
"""Module with class square that inherits from Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square"""
    def __init__(self, size):
        """Initialize the square's dimensions"""
        BaseGeometry().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method to calculate area"""
        return self.__size ** 2

    def __str__(self):
        """String representation of the Rectangle object"""
        return f"[Rectangle] {self.__size}/{self.__size}"
