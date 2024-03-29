#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""


from sys import argv
import urllib.request
with urllib.request.urlopen(argv[1]) as reqid:
    print(reqid.headers['X-Request-Id'])
