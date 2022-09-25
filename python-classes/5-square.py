#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A class that definses a square"""

    def __init__(self, size=0):
        """New Square instance
        size (int): size of the square"""
        self.__size = size

    @property
    def size(self):
        """getter-gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter-sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area-the area of the square"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """my_print - prints square"""
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(self.size):
                print("#" * self.size)
