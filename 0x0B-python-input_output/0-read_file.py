#!/usr/bin/python3

"""function """


def read_file(filename=""):
    """ function that reads a text file
    Args:
        filename(file): file tha we dear from
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
