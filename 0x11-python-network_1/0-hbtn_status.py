#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    """this code will not be executed if it was imported
    """

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status\
                                ') as response:
        data = response.read()
        utf = data.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", utf)
