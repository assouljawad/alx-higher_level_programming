#!/usr/bin/python3
""" Module represent class Rectangle,
inheritance from class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class of Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes of the instances properties
        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int): x.
            y (int): y.
            id (int): Identity of the rectangle number.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the rectangle area """
        return self.width * self.height

    def display(self):
        """ display area by symbol # """
        if self.__y > 0:
            print("\n" * self.__y, end='')
        for i in range(self.__height):
            space = " " * self.__x
            hashh = "#" * self.__width + "\n"
            print(space + hashh, end="")

    def __str__(self):
        """Prints rectangle infos"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
               self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """class Rectangle att"""
        if len(args) != 0 and args is not None:
            ls = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, ls[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """create dictionary represent the Rectangle
        Returns:
            dictionary represent the Rectangle
        """
        dic = {'x': 0, 'y': 0, 'id': 0, 'height': 0, 'width': 0}
        for key in dic:
            dic[key] = getattr(self, key)
        return dic
