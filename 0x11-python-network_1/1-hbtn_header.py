#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""


import sys
import urllib.request
arg = sys.argv[1]
with urllib.request.urlopen(arg) as reqid:
    print(reqid.headers['X-Request-Id'])
