#!/usr/bin/python3
"""Class that defines a rectangle:"""


class Rectangle:
    """A class that define a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle instance with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns recatangle area"""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns recatangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            output = ""
            for i in range(self.height):
                output += "#" * self.width
                if i < self.height - 1:
                    output += "\n"
            return output

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
