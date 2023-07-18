#!/usr/bin/python3
""" Module represent class Square,
inheritance from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class of square """

    def __init__(self, size, x=0, y=0, id=None):
        """ """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string of Square class
        Returns:
            string representation
        """
        return ("[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ size getter
        Returns:
            size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter
        Args:
            value(int): size (width / height)
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes
        Args:
            args(int): arguments
            kwargs(dict): keyworded variable of arguments length
        """
        if len(args) != 0 and args is not None:
            ls = ['id', 'width', 'x', 'y']
            for i in range(len(args)):
                setattr(self, ls[i], args[i])
                if args[i] == 'size':
                    setattr(self, "height", args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == 'size':
                    setattr(self, "height", value)

    def to_dictionary(self):
        """create dictionary represent the Square
        Returns:
            dictionary represent the Square
        """
        dic = {'id': 0, 'x': 0, 'size': 0, 'y': 0}
        for key in dic:
            if key == 'size':
                dic[key] = getattr(self, 'width')
            else:
                dic[key] = getattr(self, key)
        return dic
