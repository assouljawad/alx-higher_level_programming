#!/usr/bin/python3
"""the class-checking function."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly the same type of a given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class that we match the type of obj to.
    Returns:
        If obj a_class same type - True.
        Otherwise - False.
    """
    if type(obj) != a_class:
        return False
    return True
