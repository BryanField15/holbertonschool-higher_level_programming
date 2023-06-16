#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        #tests for finding maximum value in lists
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 2, 5, 2, 4]), 5)
        self.assertEqual(max_integer([1, 2, -3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([]), None)
