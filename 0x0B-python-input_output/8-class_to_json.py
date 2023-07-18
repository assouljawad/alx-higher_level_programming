#!/usr/bin/python3
"""function for class_to_json"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization"""

    return obj.__dict__
