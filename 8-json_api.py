#!/usr/bin/python3
""" accessing json object """

import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        values = {'q': argv[1]}
    else:
        values = {'q': ""}
    req = requests.post(url, values)
    try:
        r = req.json()
        if r != {}:
             print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
