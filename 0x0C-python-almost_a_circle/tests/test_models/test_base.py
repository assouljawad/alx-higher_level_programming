#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """class TestBase"""
    def test_the_id(self):
        """check the id"""
        Base._Base__nb_objects = 0
        bs1 = Base()
        self.assertIsNotNone(id(bs1))

    def test_the_id_2(self):
        """ Test nb object attribute """
        Base._Base__nb_objects = 0
        bs1 = Base()
        bs2 = Base()
        bs3 = Base()
        self.assertEqual(bs1.id, 1)
        self.assertEqual(bs2.id, 2)
        self.assertEqual(bs3.id, 3)

    def test_the_init(self):
        """check the instance"""
        Base._Base__nb_objects = 0
        bs1 = Base()
        self.assertIsInstance(bs1, Base)

    def test_the_numObj(self):
        """check the number of objects"""
        Base._Base__nb_objects = 0
        bs1 = Base()
        self.assertEqual(bs1.id, 1)

    def test_toJsonString_mtd(self):
        """check to_json_string methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(2, 3, 5, 5)
        aDict = rec1.to_dictionary()
        jsonString = json.dumps([aDict])
        jsonListdict = rec1.to_json_string([aDict])
        self.assertTrue(jsonString == jsonListdict)

    def test_saveToFile_mtd(self):
        """check save_to_file methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(2, 3, 5, 5)
        rec2 = Rectangle(6, 2)
        aDict = [rec1.to_dictionary(), rec2.to_dictionary()]
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as json_file:
            list_dict = json.loads(json_file.read())
        self.assertTrue(aDict == list_dict)

    def test_fromJsonString_mtd(self):
        """check from_json_string methode"""
        Base._Base__nb_objects = 0
        listInput = [{'id': 89, 'width': 6, 'height': 5},
                    {'id': 7, 'width': 8, 'height': 4}]
        jsonListInput = Rectangle.to_json_string(listInput)
        listOutput = Rectangle.from_json_string(jsonListInput)
        self.assertTrue(listInput == listOutput)

    def test_create_mtd(self):
        """check the create methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(6, 2, 5)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertFalse(rec1 == rec2)
        self.assertFalse(rec1 is rec2)

    def test_loadFromFile_mtd(self):
        """check load from file methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(5, 4, 3, 7)
        rec2 = Rectangle(4, 6)
        listRectanglesInput = [rec1, rec2]
        Rectangle.save_to_file(listRectanglesInput)
        listRectanglesOutput = Rectangle.load_from_file()
        self.assertTrue(type(listRectanglesOutput) == list)
        for rec in listRectanglesOutput:
            self.assertTrue(isinstance(rec, Rectangle))
        for rec in listRectanglesInput:
            self.assertTrue(isinstance(rec, Rectangle))
        sqr1 = Square(3)
        sqr2 = Square(8, 4, 3)
        list_squares_input = [sqr1, sqr2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output) == list)
        for sqr in list_squares_input:
            self.assertTrue(isinstance(sqr, Square))
        for sqr in list_squares_output:
            self.assertTrue(isinstance(sqr, Square))
