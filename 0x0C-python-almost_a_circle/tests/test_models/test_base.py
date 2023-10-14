#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch
""" TestClassBase """


class TestClassBase(unittest.TestCase):
    """ TestClassBase """
    
    def test_id_10(self):
        """ test_id_10 """
        self.assertEqual(Base(10).id, 10)

    def test_id(self):
        """ test_id """
        self.assertEqual(Base().id, 1)

    def test_id_2(self):
        """ test_id_2 """
        self.assertEqual(Base().id, 2)

    def test_id_neg(self):
        """ test_id_neg """
        self.assertEqual(Base(-2).id, -2)
        
    def test_id_None(self):
        """ test_id_None """
        self.assertEqual(Base(None).id, 3)

    def test_id_Var(self):
        """ test_id_Var """
        r1 = Base(100)
        self.assertEqual(r1.id, 100)

    @unittest.expectedFailure
    def test_Raise_Failure(self):
        """ test_Raise_Failure """
        id = "100"
        with self.assertRaises(TypeError):
          Base(id)

    @unittest.expectedFailure
    def test_id_Failure(self):
        """  test_id_Failure"""
        self.assertEqual(Base(15).id, 100)

    def test_id_List(self):
        """ test_id_List """
        my_list = [10, 11, 12]
        self.assertEqual(Base(my_list).id, [10, 11, 12])

    def test_id_Str(self):
        """ test_id_Str """
        self.assertEqual(Base("hi").id, "hi")

    def test_to_json_string_1(self):
        """ test_to_json_string_1 """
        r1 = Rectangle(10, 7, 2, 8, 6)
        excepted = '[{"x": 2, "y": 8, "id": 6, "height": 7, "width": 10}]'
        self.assertEqual(Base.to_json_string([r1.to_dictionary()]), excepted)

    def test_to_json_string_2(self):
        """ test_to_json_string_2 """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(3, 5, 15, 9)
        list_dict = [r1.to_dictionary(), r2.to_dictionary()]
        excepted = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, '
        excepted += '{"x": 15, "y": 9, "id": 2, "height": 5, "width": 3}]'
        self.assertEqual(Base.to_json_string(list_dict), excepted)

    def test_save_to_file_1(self):
        """ test_save_to_file_1 """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open ("Rectangle.json", "r") as file:
            file_content = file.read()
        self.assertEqual(file_content, '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')


