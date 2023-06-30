import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests for the  Base class"""

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

    def test_saving_id(self):
        """Test that checks id is correctly assigned"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_string(self):
        """Tests the method to_json_string for different input cases"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_string, str)

    def test_from_json_string(self):
        """Test for different input cases"""
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

        obj_list = Base.from_json_string("[]")
        self.assertEqual(obj_list, [])
