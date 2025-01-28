#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    This class represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes the Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # private attribute
