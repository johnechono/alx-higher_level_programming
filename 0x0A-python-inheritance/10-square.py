#!/usr/bin/python3
"""implementing the size attribute of the rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implementing a square from a rectangle"""
    def __init__(self, size):
        """initializing size of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

