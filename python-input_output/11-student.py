#!/usr/bin/python3
"""
This module defines a Student class.

Classes:
    Student: A class used to represent a Student.
"""

class Student:
    """
    A class used to represent a Student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the dictionary.
            If None, all attributes are included.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        if attrs is None:
            return {
                'age': self.age,
                'last_name': self.last_name,
                'first_name': self.first_name
            }
        else:
            return {
                attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
