#!/usr/bin/python3
""" an empty square class
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
