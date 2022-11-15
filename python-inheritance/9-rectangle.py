#!/usr/bin/python3
"""Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """new child class"""

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __init__(self, width, height):
        """initializes new instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method returns area of rectangle"""
        return self.__width * self.__height
