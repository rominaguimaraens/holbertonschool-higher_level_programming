#!/usr/bin/python3
"""Python interpreter"""


class BaseGeometry():
    """Class BaseGeometry"""

    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
