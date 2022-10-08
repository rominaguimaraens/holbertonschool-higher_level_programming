#!/usr/bin/python3
"""Python Interpreter"""


from models.base import Base

class Rectanlge(Base):
    """ Rectangle class from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(width):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(height):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def x(x):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(y):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value