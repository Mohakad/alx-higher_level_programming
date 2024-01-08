#!/usr/bin/python3
"""inherit from list"""


class MyList(list):
    """print."""

    def print_sorted(self):
        """func"""
        print(sorted(self))
