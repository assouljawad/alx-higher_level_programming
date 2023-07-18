#!/usr/bin/python3
"""class of Student"""


class Student:
    """class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ the Public instance attributes:"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method the retrieves a dictionary representation"""
        if attrs is not None:
            my_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    my_dict[i] = getattr(self, i)
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all att of the Student instance:"""

        for key, value in json.items():
            setattr(self, key, value)
