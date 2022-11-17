    #!/usr/bin/python3
"""Python Interpreter"""


class Rectangle:
    """A class Rectangle with it's attributes"""
    def __init__(self, width=0, height=0):
        """New Rectangle instance"""
        self.width = width
        self.height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        str = ""
        for row in range(self.__height):
            if row > 0:
                str += '\n'
            for col in range(self.__width):
                str += '#'
        return str

    @property
    def width(self):
        """retrieves the rectangles width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value if passes the edge cases"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves rectangles height"""
        return self.__height

    @height.setter
    def height(self, value):
        """checks value is ok, retrieves height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calcs area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calcs perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
