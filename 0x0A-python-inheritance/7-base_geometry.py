#!/usr/bin/python3
"""
a class
"""


class BaseGeometry():
    """Reprsent BaseGeometry class."""

    def area(self):
        raise Exception("area() is not implemented")

    """class don't do anything

    Raises:
            Exception: raise error if the method was called
    """

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            value (int): The parameter to validate.
            name (str): The name of the parameter.
        Raises:
            ValueError: If value is <= 0.
            TypeError: If value type is not an int.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
