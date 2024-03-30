#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as page:
            print(page.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
