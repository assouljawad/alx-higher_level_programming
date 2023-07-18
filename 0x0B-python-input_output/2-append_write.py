#!/usr/bin/python3
"""function """


def append_write(filename="", text=""):
    """ function that write in txt file
    Args:
        filename(txt): file where we will write
        text(str): test that we will add to file txt
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
