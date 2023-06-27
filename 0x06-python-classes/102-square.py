#!/usr/bin/python3
""" Creates a square class """

class Square:
    """ Defines a class square """
    def __init__(self, size=0):
        """ Initializes a square class
        Args: size=0: size of the square
         """
        self.__size = size

    @property
    def size(self):
        """ Gets the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of the square """
        return (self.__size ** 2)

    def __eq__(self, other):
        """ Compares two squares """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Compares != two squares """
        return self.area() != other.area()

    def __lt__(self, other):
        """ Compares < two squares """
        return self.area() < other.area()

    def __le__(self, other):
        """ Compares <= two squares """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Compares > two squares """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Compares >= two squares """
        return self.area() >= other.area()
