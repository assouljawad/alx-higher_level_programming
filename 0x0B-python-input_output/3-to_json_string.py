#!/usr/bin/python3
"""function"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON
    representation of an object (string):
    Args:
        my_obj: data structure that need to be encoded
    """
    return json.dumps(my_obj, sort_keys=True)
