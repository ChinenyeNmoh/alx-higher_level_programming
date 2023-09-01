#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}
    req = requests.post(url, data=values)
    print(req.text)
