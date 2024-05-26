#!/usr/bin/python3
"""
Rectancle Class
"""


class Rectangle:
    """Class of Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    """Defines Class od Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization method
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method of width"""
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    def __str__(self):
        """method string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        return str(str(self.print_symbol) * self.__width)

    def __repr__(self):
        """repr method"""
        return ("Rectangle({}, {})".format(self._width, self.__height))

    def __del__(self):
        """Delete object/instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
