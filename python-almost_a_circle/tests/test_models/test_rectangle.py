import unittest
import io
import sys

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the  Rectangle class"""

    def test_instances(self):
        """Test instantiation with valid arguments"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertIsInstance(r4, Rectangle)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

        """Test instantiation and TypeError exceptions"""
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(TypeError, Rectangle, None)
        self.assertRaises(TypeError, Rectangle, 1.1, 2.2)

        """Test instantiation and ValueError exceptions"""
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area(self):
        """Test area calculation"""
        r5 = Rectangle(2, 3)
        self.assertEqual(r5.area(), 6)

    def test_str(self):
        """Test that it returns a formatted string"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_xy(self):
        """Test disply to std out"""
        r6 = Rectangle(1, 1, 0, 0)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r6.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "#\n")

    def test_display_with_xy(self):
        """Test disply to std out with x and y greater than 0"""
        r7 = Rectangle(1, 1, 1, 1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r7.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n #\n")

    def test_update_pos_args(self):
        """Test update function with positional arguments"""
        r8 = Rectangle(1, 2, 3, 4, 5)
        r8.update(10, 20, 30, 40, 50)
        self.assertEqual(r8.id, 10)
        self.assertEqual(r8.width, 20)
        self.assertEqual(r8.height, 30)
        self.assertEqual(r8.x, 40)
        self.assertEqual(r8.y, 50)

    def test_update_key_args(self):
        """Test update function with keyword arguments"""
        r8 = Rectangle(1, 2, 3, 4, 5)
        r8.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r8.id, 10)
        self.assertEqual(r8.width, 20)
        self.assertEqual(r8.height, 30)
        self.assertEqual(r8.x, 40)
        self.assertEqual(r8.y, 50)
