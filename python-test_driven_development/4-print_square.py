#!/usr/bin/python3

"""
This module provides a function to print a square with the character #.

The print_square function takes the size of the square and prints a square
of that size using the # character.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square, must be an integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
