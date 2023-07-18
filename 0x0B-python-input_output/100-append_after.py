#!/usr/bin/python3
"""a Module for the (append_after) function"""


def append_after(filename="", search_string="", new_string=""):
    """function for Appending a line of text to a file"""
    content = ""
    with open(filename, "r", encoding="utf-8") as f:
        for each_line in f:
            content += each_line
            if search_string in each_line:
                content += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
