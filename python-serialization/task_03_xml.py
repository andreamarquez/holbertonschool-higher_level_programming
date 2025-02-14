"""
This module provides functions to serialize a Python dictionary to an XML file
and deserialize an XML file into a Python dictionary.

Functions:
    serialize_to_xml(dictionary, filename): Serialize a
    Python dictionary to an XML file.
    deserialize_from_xml(filename): Deserialize an XML
    file into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the output XML file.
    """
    root = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Parameters:
    filename (str): The name of the XML file.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except (FileNotFoundError, ET.ParseError):
        return None
