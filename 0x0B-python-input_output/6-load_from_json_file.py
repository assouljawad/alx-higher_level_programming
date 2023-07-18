#!/usr/bin/python3
"""function"""
import json


def load_from_json_file(filename):
    """ Write a function that creates an Object from
    a “JSON file”:
    Args:
        filename : json file that we will extract from it the
        json data
    """
    with open(filename, "r", encoding="UTF-8") as f:
        data = f.read()
        return json.loads(data)
