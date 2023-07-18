#!/usr/bin/python3
"""class of Student"""


class Student:
    """class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ the Public instance attributes:"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method the retrieves a dictionary representation"""

        return self.__dict__
