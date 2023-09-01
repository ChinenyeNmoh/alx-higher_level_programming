#!/usr/bin/python3
""" script to that takes in a URL, sends a
request to the URL and displays the body of the
response (decoded in utf-8) """
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
