import unittest
import io
import sys
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def test_instances_valid(self):
        """Test instantiation with valid arguments"""
        s0 = Square(1)
        s1 = Square(1, 2)
        s2 = Square(1, 2, 3)
        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s0.size, 1)
        self.assertEqual(s0.x, 0)
        self.assertEqual(s0.y, 0)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 4)

    def test_instances_type_error(self):
        """Test instantiation and TypeError exceptions"""
        self.assertRaises(TypeError, Square, "1", 2)
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 1.1, 2.2)

    def test_instances_value_error(self):
        """Test instantiation and ValueError exceptions"""
        self.assertRaises(ValueError, Square, -1, 2)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 0, 2)
        self.assertRaises(ValueError, Square, 1, 2, -3)

    def test_str(self):
        """Test that it returns a formatted string"""
        s1 = Square(5, id=1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test_area(self):
        """Test area calculation"""
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)

    def test_to_dict(self):
        """Test that a dictionary representation is returned"""
        s1 = Square(1, 2, 3, 4)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_update_pos_args(self):
        """Test update function with positional arguments"""
        s1 = Square(1, 2, 3, 4)
        s1.update(10, 20, 30, 40)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.x, 30)
        self.assertEqual(s1.y, 40)

    def test_update_key_args(self):
        """Test update function with keyword arguments"""
        s1 = Square(1, 2, 3, 4)
        s1.update(id=10, size=20, x=40, y=50)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.x, 40)
        self.assertEqual(s1.y, 50)

    def test_create_valid_dict(self):
        """Test for classmethod create with a valid dictionary for a square"""
        s1_dict = {"id": 1, "size": 3, "x": 4, "y": 5}
        s1 = Square.create(**s1_dict)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)

    def test_save_to_file_with_empty_list(self):
        """Test save_to_file method with an empty list"""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove("Square.json")

    def test_save_to_file_with_none_list(self):
        """Test save_to_file method with a None list"""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove("Square.json")

    def test_save_to_file_with_valid_list(self):
        """Test save_to_file method with a valid list"""
        s1 = Square(1, 2, id=1)
        s2 = Square(3, 4, id=2)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "size": 1, "x": 2, "y": 0}, {"id": 2, "size": 3, "x": 4, "y": 0}]')
        os.remove("Square.json")

    def test_load_from_file_not_found(self):
        """Test load_from_file method when file doesn't exist"""
        instances = Square.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_file_exists(self):
        """Test load_from_file method when file exists"""
        s1 = Square(1, 2)
        s2 = Square(3, 4)
        Square.save_to_file([s1, s2])

        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Square)
        self.assertIsInstance(instances[1], Square)

        os.remove("Square.json")
