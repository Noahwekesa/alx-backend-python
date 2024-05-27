#!/usr/bin/env python3
import unittest
from utils import access_nested_map


"""
    This is a test file for the utils module
"""


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self):
        """
        Test access_nested_map function
        """
        data = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(data, ["a", "b", "c"]), 1)
        self.assertEqual(access_nested_map(data, ["a", "b"]), {"c": 1})
        self.assertEqual(access_nested_map(data, ["a"]), {"b": {"c": 1}})
        self.assertEqual(access_nested_map(data, ["a", "b", "d"]), None)
        self.assertEqual(access_nested_map(data, ["a", "c"]), None)
        self.assertEqual(access_nested_map(data, ["a", "b", "c", "d"]), None)
