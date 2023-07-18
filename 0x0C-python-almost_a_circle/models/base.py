#!/usr/bin/python3
""" Module represent class Base """
import json
import csv


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string represent the list_dictionaries
        Args:
            list_dictionaries(dit): object
        Returns:
            The JSON string representation of the
            list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save the JSON string representation of the list_objs
        to a file
        Args:
            cls(cls): the class
            list_objs (object): list of instances
        """
        filename = cls.__name__ + ".json"
        ls = []
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                ls = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation of json_string
        Args:
            json_string (str): string representing the list of dic
        Returns:
            A list of json string
        """
        if json_string == '' or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns the instance with allthe attributes
        Args:
            dictionary (dict): A dictionary
        Returns:
            An instance with attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns all the instances in a list
        Returns:
            list of the instances
        """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, 'r', encoding="utf-8") as json_file:
                content = json_file.read()
            ls = cls.from_json_string(content)
            for data in ls:
                instance = cls.create(**data)
                instances.append(instance)
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save att in CSV file """
        filename = cls.__name__ + ".csv"
        ls = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                ls.append(obj.to_dictionary())

        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']

        if cls.__name__ == "Square":
            fieldnames = ['id', 'size', 'x', 'y']

        with open(filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(ls)

    @classmethod
    def load_from_file_csv(cls):
        """ loads att from CSV file """
        filename = cls.__name__ + ".csv"
        data = []
        instances = []
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    data.append(row)
            for att in data:
                instance = cls.create(**att)
                instances.append(instance)
            return instances
        except FileNotFoundError:
            return []
