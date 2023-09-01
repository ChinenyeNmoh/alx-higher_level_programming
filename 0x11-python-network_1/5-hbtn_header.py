#!/usr/bin/python3
""" send request using requests method and get header id """

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
