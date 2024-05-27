#!/usr/bin/env python3
import unittest
from utils import access_nested_map


"""
    This is a test file for the utils module
"""


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self):
        nested_map = {"a": {"b": {"c": 1}}}
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "c"]), 1)
        self.assertEqual(access_nested_map(nested_map, ["a", "b"]), {"c": 1})
        self.assertEqual(access_nested_map(nested_map, ["a"]), {"b": {"c": 1}})
        self.assertEqual(access_nested_map(nested_map, ["a", "b", "d"]), None)
        self.assertEqual(
            access_nested_map(nested_map, ["a", "b", "d"], default="default"), "default"
        )
        self.assertEqual(
            access_nested_map(nested_map, ["a", "b", "d"], default={"e": 2}), {"e": 2}
        )
