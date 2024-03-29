#!/usr/bin/python3
"""POST an email #0"""


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    ml = urllib.parse.urlencode({"email": sys.argv[2]}).encode('utf8')
    with urllib.request.urlopen(sys.argv[1, ml]) as req:
        print(req.read().decode('utf8'))
