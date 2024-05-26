#!/usr/bin/python3


class VerboseList(list):
    """
    SubClass of list
    """

    def append(self, el):
        """Adds an element and print message"""
        print(f"Added [{el}] to the list.")
        return super().append(el)

    def extend(self, els):
        """Adds multiple elements and print message"""
        print(f"Extended the list with [{len(els)}] items.")
        return super().extend(els)

    def remove(self, el):
        """Removes an element and print message"""
        print(f"Removed [{el}] from the list.")
        super().remove(el)

    def pop(self, index=-1):
        """Removes and returns an element at the given index"""
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
