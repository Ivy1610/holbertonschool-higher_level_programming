#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """Defines properties of Rectangle Class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle
        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter Method of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter Method of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return area of width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to return perimeter of width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Method srting object"""
        rectangle = []

        if self._width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            retangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """repr method"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete object/instance"""
        print("Bye retcangle...")
        type(self).number_of_instances -= 1
