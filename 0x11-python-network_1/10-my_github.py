#!/usr/bin/python3
"""a Python script that takes your Github credentials
(username and password) and uses the Github API to
display your id"""

import requests as rq
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'

    try:
        r = rq.get(url, auth=(argv[1], argv[2]))
        print(r.json().get('id'))

    except KeyError:
        print('None')
