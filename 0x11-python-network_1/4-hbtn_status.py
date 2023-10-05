#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    r = requests.get('https://alx-intranet.hbtn.io/status')
    conte = r.text
    print("Body response:")
    print("\t- type:", type(conte))
    print("\t- content:", conte)
