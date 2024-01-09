#!/usr/bin/python3
"""read"""


def write_file(filename="", text=""):
    """func"""
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
