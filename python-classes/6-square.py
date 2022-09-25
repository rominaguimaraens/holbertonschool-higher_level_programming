#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A class that definses a square"""

    def __init__(self, size=0, position=(0, 0)):
        """New Square instance
        size (int): size of the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """square's position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter-sets position"""
        if len(value) != 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """my_print - prints square"""
        if self.__size == 0:
            print()
            return None
        else:
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for h in range(0, self.__position[0]):
                    print(" ", end="")
                for l in range(0, self.__size):
                    print("#", end="")
                print()
