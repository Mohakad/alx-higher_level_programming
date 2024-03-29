#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""


import sys
import urllib.request

if __name__ == "__main__":
    arg = sys.argv[1]
    with urllib.request.urlopen(arg) as reqid:
        xrid = reqid.headers['X-Request-Id']
        print(xrid)
