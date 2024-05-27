#!/usr/bin/python3
def read_file(filename=""):
    """
    Defines the read_file function
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
