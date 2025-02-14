"""
This module provides basic serialization and deserialization functions.

Functions:
    serialize_and_save_to_file(data, filename): Serialize
    a Python dictionary to a JSON file.
    load_and_deserialize(filename): Load and deserialize
    a JSON file into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The name of the output JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Parameters:
    filename (str): The name of the input JSON file.

    Returns:
    dict: The deserialized dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)
