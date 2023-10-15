#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch
""" TestClassSquare """


class TestClassSquare(unittest.TestCase):
    """ TestClassSquare """

    def test_width(self):
        Base._Base__nb_objects = 0
        """ test_width """
        s1 = Square(10, 0, 0, 1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)

    def test_width_height(self):
        """ test_width_height """
        self.assertEqual(Square(10).id, 1)
        self.assertEqual(Square(2).width, 2)
        self.assertEqual(Square(3).size, 3)
        self.assertEqual(Square(10).height, 10)
        self.assertEqual(Square(8).width + Square(5).height, 13)

    def test_x(self):
        Base._Base__nb_objects = 0
        """ test_x """
        s1 = Square(2, 15, 0, 12)
        self.assertEqual(s1.x, 15)

    def test_y(self):
        """ test_y """
        s1 = Square(3, 15, 2, 12)
        self.assertEqual(s1.y, 2)

    def test_Raise_ValueError_width(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Square(-3, 2, 0, 12)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_Raise_ValueError_x(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Square(18, -5, 0, 12)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_Raise_ValueError_y(self):
        """ test_Raise_ValueError """
        with self.assertRaises(ValueError) as e:
            Square(10, 5, -100, 12)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_Raise_TypeError_width(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Square("10", 0, 0, 12)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_Raise_TypeError_x(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Square(13, "80", 0, 12)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_Raise_TypeError_y(self):
        """ test_Raise_TypeError """
        with self.assertRaises(TypeError) as e:
            Square(10, 2, "0", 12)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_Area(self):
        """ test_Area """
        s = Square(10, 2, 5, 12)
        self.assertEqual(s.area(), 100)

    def test_Area_One(self):
        """ test_Area_One """
        s = Square(1)
        self.assertEqual(s.area(), 1)

    def test_Dispaly_2x2(self):
        """ test_Dispaly_2x2 """
        s = Square(2, 0)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            s.display()
        self.assertEqual(printed.getvalue(), "##\n##\n")

    def test_Dispaly_3x2(self):
        """ test_Dispaly_3x2 """
        s = Square(3)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            s.display()
        self.assertEqual(printed.getvalue(), "###\n###\n###\n")

    def test_Dispaly_0x0(self):
        """ test_Dispaly_0x0 """
        r = Square(1, 1, 1, 15)
        r1 = Square(2, 2, 2, 12)
        r2 = Square(1, 3, 3, 12)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
            r1.display()
            r2.display()
        excepted = "\n #\n\n\n  ##\n  ##\n\n\n\n   #\n"
        self.assertEqual(printed.getvalue(), excepted)

    def test_Dispaly_4x0(self):
        """ test_Dispaly_4x0 """
        r = Square(4, 0, 0, 20)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "####\n####\n####\n####\n")

    def test_str_1(self):
        """ test_str_1 """
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Square] (12) 2/1 - 4')

    def test_str_2(self):
        """ test_str_2 """
        r1 = Square(15, 0, 0, 5)
        self.assertEqual(r1.__str__(), '[Square] (5) 0/0 - 15')

    def test_str_3(self):
        """ test_str_3 """
        r1 = Square(0, 0, 0, 0)
        self.assertEqual(r1.__str__(), '[Square] (0) 0/0 - 0/0')

    def test_Dispaly_1_2x3_2_2(self):
        """ test_Dispaly_1_2x2 """
        r = Square(2, 3, 2, 2)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "\n\n   ##\n   ##\n")

    def test_Dispaly_1_3x2(self):
        """ test_Dispaly_1_3x2 """
        r = Square(3, 2, 1, 0)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), "\n  ###\n  ###\n  ###\n")

    def test_Dispaly_1_0x0(self):
        """ test_Dispaly_1_0x0 """
        r = Square(1, 1, 0, 15)
        r1 = Square(2, 2, 2, 12)
        r2 = Square(2, 6, 2, 12)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
            r1.display()
            r2.display()
        excepted_output = " #\n\n\n  ##\n  ##\n\n\n      ##\n      ##\n"
        self.assertEqual(printed.getvalue(), excepted_output)

    def test_Dispaly_1_4x0(self):
        """ test_Dispaly_1_4x0 """
        r = Square(4, 1, 0, 20)
        with patch('sys.stdout', new_callable=StringIO) as printed:
            r.display()
        self.assertEqual(printed.getvalue(), " ####\n ####\n ####\n ####\n")

    def test_str_1(self):
        """ test_str_1 """
        r = Square(4, 15, 5, 20)
        self.assertEqual(r.__str__(), "[Square] (20) 15/5 - 4")

    def test_str_2(self):
        """ test_str_2 """
        Base._Base__nb_objects = 0
        r1 = Square(4, 1)
        self.assertEqual(r1.__str__(), "[Square] (1) 1/0 - 4")

    def test_str_3(self):
        """ test_str_3 """
        r1 = Square(12, 1, 30, 2)
        self.assertEqual(r1.__str__(), "[Square] (2) 1/30 - 12")

    def test_update_kwargs_1(self):
        """ update_kwargs_1 """
        r3 = Square(10, 10, 10, 2)
        r3.update(height=1)
        self.assertEqual(r3.__str__(), "[Square] (2) 10/10 - 10")

    def test_update_kwargs_2(self):
        """ update_kwargs_2 """
        s8 = Square(10, 10, 10, 2)
        s8.update(x=1, size=2, y=3)
        self.assertEqual(s8.__str__(), "[Square] (2) 1/3 - 2")

    def test_update_args_2(self):
        """ update_args_2 """
        s4 = Square(10, 10, 10, 2)
        s4.update(8, 10, 2, 7)
        self.assertEqual(s4.__str__(), "[Square] (8) 2/7 - 10")

    def test_Square_To_dict_1(self):
        Base._Base__nb_objects = 0
        """ test_Square_To_dict_1 """
        r4 = Square(10, 2, 1, 9)
        excepted = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(r4.to_dictionary(), excepted)

    def test_Square_To_dict_2(self):
        Base._Base__nb_objects = 0
        """ test_Square_To_dict_1 """
        r5 = Square(10, 5)
        excepted = {'id': 1, 'x': 5, 'size': 10, 'y': 0}
        self.assertEqual(r5.to_dictionary(), excepted)
