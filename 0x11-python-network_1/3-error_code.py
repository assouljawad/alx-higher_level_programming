#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    try:
        with urllib.request.urlopen(argv[1]) as response:
            decoded = response.read().decode("utf-8")
            print(decoded)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
