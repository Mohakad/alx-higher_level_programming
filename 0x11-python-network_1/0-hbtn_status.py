#!/usr/bin/python3
"""Python script that fetches url"""


import urllib.request
dt = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(dt) as resp:
    data = resp.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf8')))
