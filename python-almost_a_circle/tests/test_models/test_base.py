import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def test_auto_id_assignment(self):
        """Test that Base assigns a unique ID"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertNotEqual(b1.id, b2.id)

    def test_auto_id_assignment_plus_one(self):
        """Test that checks  ID's are sequential"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id + 1, b2.id)
        self.assertEqual(b2.id + 1, b3.id)
