#!/usr/bin/python3
"""script that get the sha and the owner of the commit
"""
import requests
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    if len(argv) > 1:
        url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])
        try:
            r = requests.get(url)
            i = 0
            for data in r.json():
                owner = data['commit']['author']['name']
                sha = data['sha']
                print("{}: {}".format(sha, owner))
                if i == 9:
                    break
                i += 1
        except Exception:
            pass
