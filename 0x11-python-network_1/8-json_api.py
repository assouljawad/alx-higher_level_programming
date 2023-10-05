#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    q = ""
    if len(argv) > 1:
        q = argv[1]

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
        data = r.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
