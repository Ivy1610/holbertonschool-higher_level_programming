#!/usr/bin/python3
"""Defines a square"""


class Square:

    """Square class"""

    def __init__(self, size=0):
        """Initialization method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """square value"""
        return self.__size**2
