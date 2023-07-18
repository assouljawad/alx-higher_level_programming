#!/usr/bin/python3
"""
a class
"""


class BaseGeometry():
    """class don't do anything

    Raises:
            Exception: raise error if the method was called
    """
    def area(self):
        raise Exception("area() is not implemented")
