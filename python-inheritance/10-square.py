#!/usr/bin/python3
"""Python interpreter"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New child class of Rectangle"""

    def __init__(self, size):
        """Initialize new instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area"""
        return self.__size * self.__size
