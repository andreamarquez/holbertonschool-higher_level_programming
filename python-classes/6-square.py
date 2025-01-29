#!/usr/bin/python3
"""
This module defines a class Square that represents a square.

The Square class includes:
- A private instance attribute `__size` to store the size of the square.
- A private instance attribute `__position` to store the position of
the square.
- A constructor to initialize the size and position with validation.
- A property to retrieve the size.
- A property setter to set the size with validation.
- A property to retrieve the position.
- A property setter to set the position with validation.
- A method to calculate the area of the square.
- A method to print the square with the character #.
"""


class Square:
    """
    This class represents a square with private size and position attributes.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square with a given size and position.

        Args:
            size (int): The size of the square. Must be an integer >= 0.
            position (tuple): The position of the square. Must be a
            tuple of 2 positive integers.

        Raises:
            TypeError: If size is not an integer or position is not a
            tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter for validation
        self.position = position  # Use the setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The position of the square. Must be a
            tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
