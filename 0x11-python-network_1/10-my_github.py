#!/usr/bin/python3
"""script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    if len(argv) > 1:
        url = "https://api.github.com/users/{}".format(argv[1])
        headers = {'Authorization': 'Bearer {}'.format(
            argv[2]), "X-GitHub-Api-Version": "2022-11-28",
            'Accept': 'application/vnd.github+json'}
        try:
            r = requests.get(url, headers=headers)
            print(r.json()['id'])
        except Exception:
            print('None')
