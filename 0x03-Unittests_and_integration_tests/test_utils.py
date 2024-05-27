#!/usr/bin/env python3
"""
This is a test file for the utils module
"""

import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, ("a",)),
            ({"a": {"b": 2}}, ("a",)),
            ({"a": {"b": 2}}, ("a", "b")),
        ]
    )
    def test_access_map(self, nested_map, path):
        expected_value = nested_map.get(path[0])
        for key in path[1:]:
            expected_value = expected_value.get(key)
        self.assertEqual(expected_value, access_nested_map(nested_map, path))
