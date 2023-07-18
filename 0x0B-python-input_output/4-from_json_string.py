#!/usr/bin/python3
"""function"""
import json


def from_json_string(my_str):
    """  function that returns an object (Python data structure)
    represented by a JSON string:
    Args:
        my_str: JSON string that will be decoded
    """
    data = json.loads(my_str)
    return data
