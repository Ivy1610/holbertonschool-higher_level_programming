#!/usr/bin/python3


class CountedIterator:
    """
    Class to create a counted iterator
    """

    def __init__(self, _iterable):
        """Initializes the CountedIterator with the given iterable object

        Args:
            _iterable: The iterable object to iterate over
        """
        self.iterator = iter(_iterable)
        self.count = 0

    def get_count(self):
        """Returns the current count of iterations"""
        return self.count

    def __next__(self):
        """Returns the next element from the iterable"""
        item = next(self.iterator)
        self.count += 1
        return item
