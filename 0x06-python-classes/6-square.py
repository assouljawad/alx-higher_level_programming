#!/usr/bin/python3
""" define a class Square"""


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the new square.

        Args:
            size (int): The size of new square.
            position (int, int): The position of new square.
        """
        self.size = size
        self.position = position

    def area(self):
        x = self.__size * self.__size
        return x

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            print("#"*self.__size)
