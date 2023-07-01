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
