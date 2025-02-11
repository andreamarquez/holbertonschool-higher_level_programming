#!/usr/bin/python3

"""
This module provides a function that writes an object to a
text file, using a JSON representation.

Functions:
    save_to_json_file(my_obj, filename): Writes an object to a
    text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
