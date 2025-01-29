#!/usr/bin/python3
class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize the square with an optional size argument.
        :param size: The size of the square's side.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        :return: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieve the size of the square.
        :return: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        :param value: The new size of the square's side.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
