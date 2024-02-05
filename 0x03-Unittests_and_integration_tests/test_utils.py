#!/usr/bin/env python3
''' unittest '''
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    ''' parameter '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Tuple[str],
            expected: Union[Mapping, int]) -> None:
        ''' test '''
        self.assertEqual(access_nested_map, (nested_map), path, expected)
