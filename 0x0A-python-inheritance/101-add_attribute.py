#!/usr/bin/python3
"""Defines function adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to object if it's possible.

    Args:
        obj (any): The object to add tha will be added.
        att (str): The name of the att.
        value (any): The value of the att.
    Raises:
        TypeError: If the attribute is possible be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
