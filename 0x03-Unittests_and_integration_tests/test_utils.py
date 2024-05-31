#!/usr/bin/env python3
"""
This is a test file for the utils module
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TaskAccessNestedMap(unittest.TestCase):
    """
    This class tests the access_nested_map function
    """

    @parameterized.expand(
        [
            ({"a": 1, "b": {"c": 2}}, ["a"], 1),
            ({"a": 1, "b": {"c": 2}}, ["b", "c"], 2),
            ({"a": 1, "b": {"c": 2}}, ["a", "b"], None),
            ({"a": 1, "b": {"c": 2}}, ["c", "d"], None),
        ]
    )
    def test_access_nested_map(self):
        """
        This method tests the access_nested_map function
        """
        data = {"a": 1, "b": {"c": 2}}
        self.assertEqual(access_nested_map(data, ["a"]), 1)
        self.assertEqual(access_nested_map(data, ["b", "c"]), 2)
        self.assertIsNone(access_nested_map(data, ["a", "b"]))
        self.assertIsNone(access_nested_map(data, ["c", "d"]))

    @parameterized.expand([(None, ["a", "b"], None)])
    def test_access_nested_map_exception(self):
        """
        This method tests the access_nested_map function with exception
        """
        data = {"a": 1, "b": {"c": 2}}
        with self.assertRaises(KeyError):
            access_nested_map(data, ["a", "b"], "c")
