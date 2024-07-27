#!/usr/bin/python3
"""
    Class MyList that inherits from list
"""


class MyList(list):
    """
        class that inherits from list

    Args:
        list: class list
    """

    def print_sorted(self):
        """Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
