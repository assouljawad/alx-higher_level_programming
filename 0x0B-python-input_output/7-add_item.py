#!/usr/bin/python3
"""function for saving to json"""
import sys


if __name__ == "__main__":
    """function for saving to json"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        ls = load_from_json_file("add_item.json")
    except FileNotFoundError:
        ls = []
    ls.extend(sys.argv[1:])
    save_to_json_file(ls, "add_item.json")
