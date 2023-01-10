#!/usr/bin/python3
"""square"""


class Square:
    """square"""
    def __init__(self, size=0):
        self.size = size

    def self(size):
        """get size"""
        return self.__size
    def __init__(self, value):
        """data"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
