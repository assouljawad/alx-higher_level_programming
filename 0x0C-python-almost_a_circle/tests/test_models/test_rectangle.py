#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """class the TestRectangle"""
    def test_the_id(self):
        """check the id"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(6, 4)
        self.assertIsNotNone(id(rec1))

    def test_the_init(self):
        """check the instances created state"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6)
        self.assertIsInstance(rec1, Rectangle)

    def test_num_obj(self):
        """check number of the objects"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(6, 4, 1, 1)
        rec2 = Rectangle(7, 7)
        self.assertEqual(rec2.id, 2)

    def test_getter_and_setter(self):
        """check the getter and the setter"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 5, 1, 1)
        self.assertEqual(rec1.width, 4)
        self.assertEqual(rec1.height, 5)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 1)

    def test_the_errors(self):
        """checks the invalid attributes"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec1.width = "4"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec1.width = -4
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec1.height = "6"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec1.height = -6
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec1.x = "1"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 6, -1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec1.y = "1"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 6, 1, -1)

    def test_display_mtd(self):
        """checks the display methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 5)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        rec1.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString,
                         "####\n####\n####\n####\n####\n")

    def test_area_mtd(self):
        """checks the area methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6)
        self.assertEqual(rec1.area(), rec1.width * rec1.height)

    def test_str(self):
        """checks str"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6, 1, 1, 6)
        rec2 = Rectangle(4, 6, 1)
        string_1 = rec1.__str__()
        string_2 = rec2.__str__()
        self.assertEqual(string_1,
                         "[Rectangle] (6) 1/1 - 4/6")
        self.assertEqual(string_2,
                         "[Rectangle] (1) 1/0 - 4/6")

    def test_display_x_and_y(self):
        """checks display x & y"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 3, 1, 2)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        rec1.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, "\n\n ####\n ####\n ####\n")
        rec2 = Rectangle(4, 2, 1, 0)
        oldStdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        rec2.display()
        sys.stdout = oldStdout
        resultString = result.getvalue()
        self.assertEqual(resultString, " ####\n ####\n")

    def test_update_mtd(self):
        """checks update methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(5, 5, 5, 5)
        rec1.update(2)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (2) 5/5 - 5/5")
        rec1.update(2, 2)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (2) 5/5 - 2/5")
        rec1.update(2, 2, 3)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (2) 5/5 - 2/3")
        rec1.update(2, 2, 3, 6)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (2) 6/5 - 2/3")
        rec1.update(2, 2, 3, 6, 7)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (2) 6/7 - 2/3")

    def test_update_kwargs_mtd(self):
        """checks update by kwargs """
        Base._Base__nb_objects = 0
        rec1 = Rectangle(5, 5, 5, 5)
        rec1.update(height=1)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 5/5 - 5/1")
        rec1.update(width=1, x=2)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 2/5 - 1/1")
        rec1.update(y=2, width=6, x=4, id=7)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (7) 4/2 - 6/1")
        rec1.update(x=2, height=4, y=5, width=7)
        string = rec1.__str__()
        self.assertEqual(string, "[Rectangle] (7) 2/5 - 7/4")

    def test_dictionary_mtd(self):
        """checks dictionary methode"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6, 2, 1)
        rec1_dictionary = rec1.to_dictionary()
        a_dict = {'x': 2, 'y': 1, 'id': 1, 'height': 6, 'width': 4}
        self.assertTrue(rec1_dictionary == a_dict)

    def test_the_empty(self):
        """check the empty arguments"""
        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec1.width = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec1.width = "6"
