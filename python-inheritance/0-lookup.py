#!/usr/bin/python3
"""
    function that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """
        function that returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of a class

    return:
        List of attributes
    """

    return dir(obj)
