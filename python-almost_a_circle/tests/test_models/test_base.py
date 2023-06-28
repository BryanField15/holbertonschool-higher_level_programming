"""Unit test for class Base"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests for Base class"""

    def test_auto_id_assignment(self):
        """Test that Base assigns a unique ID"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
