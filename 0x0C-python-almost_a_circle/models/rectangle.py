#!/usr/bin/python3
"""Rectangle that inherits from Base:"""
from models.base import Base


class Rectangle(Base):
    """class rect"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
