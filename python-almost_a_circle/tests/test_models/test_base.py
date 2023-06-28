import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Tests for Base class
    """

    def test_auto_assign_id(self):
        """
        Test that Base assigns a unique ID
        """
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)
