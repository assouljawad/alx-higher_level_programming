#!/usr/bin/python3
"""Defines the class Rectangle that inherits from the
1BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle class."""

    def __init__(self, width, height):
        """Represent a rectangle using BaseGeometry."""

        """Intialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return:
                the area for the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return str() representation of a Rectangle."""
        name = self.__class__.__name__
        return ("[{}] {}/{}".format(name, self.__width, self.__height))
