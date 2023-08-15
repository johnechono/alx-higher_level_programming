#!/usr/bin/python3
"""will modify the string representation of the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defineing a Square class"""
    def __init__(self, size):
        """instantiating and validating attributes
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
