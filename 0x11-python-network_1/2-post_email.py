#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        decoded = response.read().decode('utf-8')
        print(decoded)
