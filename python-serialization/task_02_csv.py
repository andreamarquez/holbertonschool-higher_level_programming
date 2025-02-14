"""
This module provides a function to convert a CSV file to JSON format.

Functions:
    convert_csv_to_json(csv_filename): Convert a CSV file to
    JSON format and save it as data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it as data.json.

    Parameters:
    csv_filename (str): The filename of the input CSV file.

    Returns:
    bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
