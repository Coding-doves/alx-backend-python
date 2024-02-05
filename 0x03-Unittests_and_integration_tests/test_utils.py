#!/usr/bin/env python3
''' unittest '''
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Tuple, Union, Type, Dict


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
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Tuple[str],
            expected: Type[Exception]) -> None:
        ''' testing '''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' TestGetjson '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict[str, bool]) -> None:
        ''' testing '''
        with patch("requests.get") as mock:
            mock.return_value.json.return_value = test_payload

            self.assertEqual(get_json(test_url), test_payload)

            mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    ''' TestMemoize '''
    def test_memoize(self):
        ''' testing '''

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as a_mk:
            test = TestClass()
            test.a_property
            test.a_property
            a_mk.assert_called_once()
