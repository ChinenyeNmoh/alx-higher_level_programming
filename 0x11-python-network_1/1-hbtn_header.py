#!/usr/bin/python3
""" script to fetch id from a requested url """


if __name__ == '__main__':
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        print(response.headers.get('x-request-id'))
