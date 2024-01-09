#!/usr/bin/python3
"""read"""


def append_write(filename="", text=""):
    """func"""
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
