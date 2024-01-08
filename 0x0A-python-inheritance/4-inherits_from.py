#!/usr/bin/python3
"""inherited from"""


def inherits_from(obj, a_class):
    """inherited instance of a class.

    Args:
        obj (any): object
        a_class (type): class
    Returns:
        True or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
