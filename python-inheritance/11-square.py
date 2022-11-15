#!/usr/bin/python3
"""Python interpreter"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New child class of Rectangle"""

    def __init__(self, size):
        """Initialize a new instance"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Area"""
        return self.__size * self.__size
