#!/usr/bin/python3

"""
This module provides a function to add two integers or floats.

The add_integer function takes two arguments, a and b, and returns
their sum as an integer.
If either argument is not an integer or float, a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or b != b:  # Check for NaN
        raise ValueError("cannot convert float NaN to integer")
    # Check for infinity
    if abs(a) == float('inf') or abs(b) == float('inf'):
        raise OverflowError("value too large to convert to int")
    
    # Check for large float values
    if abs(a) > 1e308 or abs(b) > 1e308:
        raise OverflowError("value too large to convert to int")
    
    sum_ab = int(a) + int(b)
    if abs(sum_ab) > 1e308:  # Check for overflow in the sum
        raise OverflowError("sum too large to convert to int")
    return sum_ab
