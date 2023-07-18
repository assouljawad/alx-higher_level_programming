#!/usr/bin/python3
"""a class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of,
    or if the object is an instance of a class given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class that we match the type of obj to.
    Returns:
        If obj a_class same type - True.
        Otherwise - False.
    """
    if not isinstance(obj, a_class):
        return False
    return True
