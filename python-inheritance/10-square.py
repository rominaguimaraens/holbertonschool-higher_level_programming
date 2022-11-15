#!/usr/bin/python3
"""Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new square child of rectangle"""

    def __init__(self, size):
        """initialize new instance Square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area"""
        return self.__size * self.__size
