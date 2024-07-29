#!/usr/bin/env python3
""" This module contains unit tests for a access_nested_map function """
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """
        This class is a unittest for access_nested_map function.
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), (1)),
            ({"a": {"b": 2}}, ("a",), ({"b": 2})),
            ({"a": {"b": 2}}, ("a", "b"), (2))
            ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with different nested maps and paths.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
            expected: The expected value from the nested map.

        Asserts:
            The value obtained from access_nested_map is equal to the
            expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",), ("a")),
            ({"a": 1}, ("a", "b"), ("b"))
            ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map with different nested maps and paths.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
            expected: The expected value from the nested map.

        Asserts:
            A KeyError is raised when the path does not exist
            in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected)


class TEstGetJson(unittest.TestCase):
    """
        This class is a mock unittest for get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
            Test get_json function returns the correct pyload and ensure the
            get method is called only once per url.

            Args:
                test_url (str): the URL.
                test_payload (dict): the returned dict.
                mock_get (MagickMock): the mocked requests.get method.

            Asserts:
                The payload returned by the mocked requests.
                The requests.get method was called exactly once per URL.
        """
        mock_res = MagicMock(status_code=200)
        mock_res.json.return_value = test_payload
        mock_get.return_value = mock_res
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
