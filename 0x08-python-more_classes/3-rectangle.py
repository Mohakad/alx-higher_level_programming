#!/usr/bin/python3
"""rectangle """


class Rectangle:
    """class"""
    def __init__(self, width=0, height=0):
        """init"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrive"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """rectangle perimeter:"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """#"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        hsh = []
        for h in range(self.__height):
            [hsh.append('#') for w in range(self.__width)]
            if h != self.__height - 1:
                hsh.append("\n")
        return ("".join(hsh))
