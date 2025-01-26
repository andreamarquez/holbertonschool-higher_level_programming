#!/usr/bin/python3

"""
This module provides a function to format text with specific indentation.

The text_indentation function takes a string and prints the text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be formatted, must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end="")
