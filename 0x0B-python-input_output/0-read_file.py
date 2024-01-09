#!/usr/bin/python3
"""read"""


def read_file(filename=""):
    """func"""
    with open(filename, encoding="UTF8") as fl:
        print(fl.read())
