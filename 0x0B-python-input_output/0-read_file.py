#!/usr/bin/python3
"""read"""


def read_file(filename=""):
    """func"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read())
