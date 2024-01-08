#!/usr/bin/python3
"""class check"""


def is_same_class(obj, a_class):
    """nstance of a class.

    Args:
        obj (any): object
        a_class (type): class
    Returns:
        True or False.
    """
    if type(obj) == a_class:
        return True
    return False
