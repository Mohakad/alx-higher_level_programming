#!/usr/bin/python3
"""class Square that defines a square
    """


class Square:
    """square
    """
    def __init__(self, size=0):
        """size must be an integer,

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
