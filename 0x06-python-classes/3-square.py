#!/usr/bin/python3
"""Square"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """new square
        Args:
            size (int): size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of the squar"""
        return (self.__size * self.__size)
