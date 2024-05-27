#!/usr/bin/python3
"""Module containing function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written

    Args:
        filename (str, optional): name of the file
        text (str, optional): string of text to write to file

    Returns:
        int: number of characters written to file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
