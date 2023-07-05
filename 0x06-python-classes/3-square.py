#!/usr/bin/python3
""" define a class Square"""


class Square:
    """ Square class """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        x = self.__size ** 2
        return x
