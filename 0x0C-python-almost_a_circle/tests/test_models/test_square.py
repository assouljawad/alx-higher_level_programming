#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """class TestSquare"""
    def test_the_id(self):
        """check instance id"""
        Base._Base__nb_objects = 0
        sqr1 = Square(2)
        self.assertIsNotNone(id(sqr1))

    def test_the_init(self):
        """check instance"""
        Base._Base__nb_objects = 0
        sqr1 = Square(2)
        self.assertIsInstance(sqr1, Square)
        self.assertTrue(issubclass(type(sqr1), Rectangle))

    def test_num_obj(self):
        """check the number of the instances"""
        Base._Base__nb_objects = 0
        sqr1 = Square(2, 2)
        sqr2 = Square(6, 4)
        self.assertEqual(sqr2.id, 2)

    def test_getterAndSetter_mtd(self):
        """check the getter and setter methods"""
        Base._Base__nb_objects = 0
        sqr1 = Square(4)
        self.assertEqual(sqr1.width, 4)
        self.assertEqual(sqr1.height, 4)
        sqr1 = Square(4, 6)
        self.assertEqual(sqr1.width, 4)
        self.assertEqual(sqr1.height, 4)
        self.assertEqual(sqr1.x, 6)
        sqr1 = Square(4, 2, 6)
        self.assertEqual(sqr1.width, 4)
        self.assertEqual(sqr1.height, 4)
        self.assertEqual(sqr1.x, 2)
        self.assertEqual(sqr1.y, 6)

    def test_area_mtd(self):
        """check area methode"""
        Base._Base__nb_objects = 0
        sqr1 = Square(6)
        self.assertEqual(sqr1.area(), sqr1.width * sqr1.height)

    def test_the_errors(self):
        """check the errors"""
        Base._Base__nb_objects = 0
        sqr1 = Square(6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr1.size = "6"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr1.size = -6
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr1.x = "4"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr1.x = -4
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr1.y = "4"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(4, 6, -4)

    def test_display_mtd(self):
        """check the display methode"""
        Base._Base__nb_objects = 0
        sqr1 = Square(4)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        sqr1.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, "####\n####\n####\n####\n")
        sqr2 = Square(3, 1)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        sqr2.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, " ###\n ###\n ###\n")
        sqr3 = Square(2, 1, 2)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        sqr3.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, "\n\n ##\n ##\n")

    def test_str_mtd(self):
        """check str methode"""
        Base._Base__nb_objects = 0
        sqr1 = Square(4)
        sqr2 = Square(3, 4)
        sqr3 = Square(4, 2, 4)
        string_1 = sqr1.__str__()
        string_2 = sqr2.__str__()
        string_3 = sqr3.__str__()
        self.assertEqual(string_1, "[Square] ({:d}) 0/0 - 4".format(sqr1.id))
        self.assertEqual(string_2, "[Square] ({:d}) 4/0 - 3".format(sqr2.id))
        self.assertEqual(string_3, "[Square] ({:d}) 2/4 - 4".format(sqr3.id))

    def test_display_x_and_y(self):
        """check the display in x & y att"""
        Base._Base__nb_objects = 0
        sqr1 = Square(3, 3, 3)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        sqr1.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, "\n\n\n   ###\n   ###\n   ###\n")
        s2 = Square(2, 2, 1)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        s2.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, "\n  ##\n  ##\n")

    def test_update_mtd(self):
        """check the kwargs"""
        Base._Base__nb_objects = 0
        sqr1 = Square(6)
        sqr1.update(2)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (2) 0/0 - 6")
        sqr1.update(2, 4)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (2) 0/0 - 4")
        sqr1.update(4, 2, 4)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (4) 4/0 - 2")
        sqr1.update(4, 2, 3, 1)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (4) 3/1 - 2")
        sqr1.update(y=20)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (4) 3/20 - 2")
        sqr1.update(size=4, x=1)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (4) 1/20 - 4")
        sqr1.update(size=5, id=22, y=2)
        string = sqr1.__str__()
        self.assertEqual(string, "[Square] (22) 1/2 - 5")

    def test_dictionary_mtd(self):
        """check the dictionary"""
        Base._Base__nb_objects = 0
        sqr1 = Square(4, 3, 4, 1)
        a_dict = {'id': 1, 'x': 3, 'size': 4, 'y': 4}
        sqr1_dictionary = sqr1.to_dictionary()
        self.assertTrue(sqr1_dictionary == a_dict)

    def test_empty_mtd(self):
        """check the empty arguments"""
        Base._Base__nb_objects = 0
        sqr1 = Square(7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr1.size = "7"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr1.size = None
