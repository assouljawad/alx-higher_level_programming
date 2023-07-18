#!/usr/bin/python3
"""a class-checking function."""


def inherits_from(obj, a_class):
    """
     is an instance of a class that inherited
     (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class that we match the type of obj to.
    Returns:
        If obj a_class same type - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
