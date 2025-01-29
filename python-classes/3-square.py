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

    def __init__(self, size=0):
        """
        Initializes the Square with a given size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private attribute

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
