#!/usr/bin/python3
"""class and inherited class"""


def is_kind_of_class(obj, a_class):
    """is an instance or inherited

    Args:
        obj (any): object
        a_class (type): class
    Returns:
        True or False.
    """
    if isinstance(obj, a_class):
        return True
    return False
