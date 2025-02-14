#!/usr/bin/python3
"""
This module provides a custom class with serialization and deserialization
capabilities using the pickle module.

Classes:
    CustomObject: A class used to represent a custom object with attributes
    name, age, and is_student, and methods to serialize and
    deserialize the object.
"""

import pickle


class CustomObject:
    """
    A class used to represent a custom object.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Whether the object is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject instance with name, age, and is_student.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display object attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save to a file.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file to load the
            serialized object from.

        Returns:
            CustomObject: The deserialized object.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
