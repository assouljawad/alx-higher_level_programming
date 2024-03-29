#!/usr/bin/python3
"""script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    data = {}
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code:", r.status_code)
