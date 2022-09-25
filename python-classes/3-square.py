#!/usr/bin/python3
""" a square class
"""


class Square:
    """A class that definses a square
    """
    def __init__(self, size=0):
        """__init__
        __init__ initializes size
        Attributes:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area
        the area of the square
        """
        area = self.__size * self.__size
        return area
