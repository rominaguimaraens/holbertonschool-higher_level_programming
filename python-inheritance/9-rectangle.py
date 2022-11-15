#!/usr/bin/python3
"""Python interpreter"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """New child class"""

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __init__(self, width, height):
        """Initializes a new instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area"""
        return self.__width * self.
