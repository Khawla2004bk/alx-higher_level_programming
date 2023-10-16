#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
""" TestClassRecatngle """


class TestClassRectangle(unittest.TestCase):
    """ TestClassRectangle """

    def test_width(self):
        Base._Base__nb_objects = 0
        """ test_width """
        r1 = Rectangle(10, 2, 0, 0, None)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)

    def test_width_height(self):
        """ test_width_height """
        self.assertEqual(Rectangle(10, 12).id, 2)
        self.assertEqual(Rectangle(1, 12).width, 1)
        self.assertEqual(Rectangle(10, 12).height, 12)
        self.assertEqual(Rectangle(8, 6).width + Rectangle(5, 1).height, 9)

    def test_x(self):
        Base._Base__nb_objects = 0
        """ test_x """
        r1 = Rectangle(10, 2, 15, 0, 12)
        self.assertEqual(r1.x, 15)

    def test_y(self):
        """ test_y """
        r1 = Rectangle(10, 2, 15, 2, 12)
        self.assertEqual(r1.y, 2)

    def test_Raise_ValueError_width(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Rectangle(-3, 2, 0, 0, 12)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_Raise_ValueError_height(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2, 0, 0, 12)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_Raise_ValueError_width_Zero(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Rectangle(0, -2, 0, 0, 12)
        self.assertEqual(str(e.exception), "width must be > 0")
    
    def test_Raise_ValueError_height_Zero(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Rectangle(2, 0, 0, 0, 12)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_Raise_ValueError_x(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -5, 0, 12)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_Raise_ValueError_y(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 5, -100, 12)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_Raise_TypeError_width(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2, 0, 0, 12)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_Raise_TypeError_height(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2", 0, 0, 12)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_Raise_TypeError_x(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, "80", 0, 12)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_Raise_TypeError_y(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 5, "0", 12)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_Area(self):
        """ test_Area """
        r = Rectangle(10, 2, 5, 0, 12)
        self.assertEqual(r.area(), 20)

    def test_Area_Zero(self):
        """ test_Area_Zero """
        r = Rectangle(10, 1)
        self.assertEqual(r.area(), 10)

    def test_Dispaly_2x2(self):
        """ test_Dispaly_2x2 """
        r = Rectangle(2, 2)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "##\n##\n")

    def test_Dispaly_3x2(self):
        """ test_Dispaly_3x2 """
        r = Rectangle(3, 2)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "###\n###\n")

    def test_Dispaly_0x0(self):
        """ test_Dispaly_0x0 """
        r = Rectangle(1, 1, 0, 0, 15)
        r2 = Rectangle(1, 6, 0, 0, 12)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
            r2.display()
        self.assertEqual(printed.getvalue(), "#\n#\n#\n#\n#\n#\n#\n")

    def test_Dispaly_4x0(self):
        """ test_Dispaly_4x0 """
        r = Rectangle(4, 1, 0, 0, 20)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "####\n")

    def test_str_1(self):
        """ test_str_1 """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

    def test_str_2(self):
        """ test_str_2 """
        r1 = Rectangle(2, 15, 0, 0, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (5) 0/0 - 2/15')

    def test_str_3(self):
        """ test_str_3 """
        r1 = Rectangle(1, 1, 0, 0, 0)
        self.assertEqual(r1.__str__(), '[Rectangle] (0) 0/0 - 1/1')

    def test_Dispaly_1_2x3_2_2(self):
        """ test_Dispaly_1_2x2 """
        r = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_Dispaly_1_3x2(self):
        """ test_Dispaly_1_3x2 """
        r = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), " ###\n ###\n")

    def test_Dispaly_1_0x0(self):
        """ test_Dispaly_1_0x0 """
        r = Rectangle(1, 2, 1, 0, 15)
        r1 = Rectangle(1, 1, 0, 2, 12)
        r2 = Rectangle(1, 3, 3, 2, 12)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
            r1.display()
            r2.display()
        excepted_output = " #\n #\n\n\n#\n\n\n   #\n   #\n   #\n"
        self.assertEqual(printed.getvalue(), excepted_output)

    def test_Dispaly_1_4x0(self):
        """ test_Dispaly_1_4x0 """
        r = Rectangle(4, 1, 0, 0, 20)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "####\n")

    def test_str_1(self):
        """ test_str """
        r = Rectangle(4, 1, 15, 5, 20)
        self.assertEqual(r.__str__(), "[Rectangle] (20) 15/5 - 4/1")

    def test_str_2(self):
        """ test_str """
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 0/0 - 4/1")

    def test_str_3(self):
        """ test_str """
        r1 = Rectangle(12, 1, 30, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 30/2 - 12/1")

    def test_update_kwargs_1(self):
        """ update_kwargs_1 """
        r3 = Rectangle(10, 10, 10, 10, 2)
        r3.update(height=1)
        self.assertEqual(r3.__str__(), "[Rectangle] (2) 10/10 - 10/1")

    def test_update_kwargs_2(self):
        """ update_kwargs_2 """
        r4 = Rectangle(10, 10, 10, 10, 2)
        r4.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r4.__str__(), "[Rectangle] (2) 1/3 - 4/2")

    def test_update_args_2(self):
        """ update_kwargs_2 """
        r4 = Rectangle(10, 10, 10, 10, 2)
        r4.update(8, 10, 12, 2, 7)
        self.assertEqual(r4.__str__(), "[Rectangle] (8) 2/7 - 10/12")

    def test_Rectangle_To_dict_1(self):
        Base._Base__nb_objects = 0
        """ test_Rectangle_To_dict_1 """
        r4 = Rectangle(10, 2, 1, 9)
        excepted = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r4.to_dictionary(), excepted)

    def test_Rectangle_To_dict_2(self):
        Base._Base__nb_objects = 0
        """ test_Rectangle_To_dict_1 """
        r5 = Rectangle(10, 5)
        excepted = {'x': 0, 'y': 0, 'id': 1, 'height': 5, 'width': 10}
        self.assertEqual(r5.to_dictionary(), excepted)

    def test_create_1(self):
        Base._Base__nb_objects = 0
        """ test_case : method def create(cls, **dictionary): that returns an instance with all attributes already set"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_json_to_string_1(self):
        Base._Base__nb_objects = 0
        """ test_json_to_string_1 """
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_input, list))
        self.assertTrue(isinstance(json_list_input, str))
        self.assertTrue(isinstance(list_output, list))
        self.assertEqual(json_list_input,'[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')
        self.assertEqual(list_output,[{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}])

    def test_save_to_file(self):
        Base._Base__nb_objects = 0
        """ test_save_to_file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),'[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]')
            print(file.read())
    def test_load_from_file(self):
        Base._Base__nb_objects = 0
        """ test_save_to_file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        for rect_input, rect_output in zip(list_rectangles_input, list_rectangles_output):
            self.assertEqual(rect_input.x, rect_output.x)
            self.assertEqual(rect_input.y, rect_output.y)
            self.assertEqual(rect_input.width, rect_output.width)
            self.assertEqual(rect_input.height, rect_output.height)

    def test_save_to_file_1(self):
        Base._Base__nb_objects = 0
        """ test_save_to_file1 """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file1:
            self.assertEqual(file1.read(),'[]')


    def test_save_to_file_2(self):
        """ test_save_to_file_2 """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file2:
            self.assertEqual(file2.read(),'[]')
