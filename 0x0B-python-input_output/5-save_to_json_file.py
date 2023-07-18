#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """ function that returns the JSON
    representation of an object (string):
    Args:
        my_obj: data structure that need to be encoded
        filename : txt file where we will write
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
