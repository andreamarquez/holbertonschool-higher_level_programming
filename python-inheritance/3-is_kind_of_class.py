#!/usr/bin/python3
"""
This module defines a function `is_kind_of_class` that checks if an object
is an instance of, or if the object is an instance of a class that
inherited from, the specified class.

The `is_kind_of_class` function:
- Takes an object and a class as arguments.
- Returns True if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise
    False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of or inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
