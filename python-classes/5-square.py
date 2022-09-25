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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area
        the area of the square
        """
        area = self.__size * self.__size
        return area

	def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
