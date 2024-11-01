#!/usr/bin/env python3
"""test_utls.py
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """test_access_nested_map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson
    """
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests.get') as mock:
            mock_response = Mock()
            mock_response.json = Mock(return_value=test_payload)
            mock.return_value = mock_response
            result = get_json(test_url)
            mock.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize
    """

    def test_memoize(self):
        """test_memoize
        """
        class TestClass:
            """TestClass
            """

            def a_method(self):
                """a_mehod
                """
                return 42

            @memoize
            def a_property(self):
                """a_property
                """
                return self.a_method()
        x = TestClass()
        with patch.object(x, 'a_method') as cm:
            cm.return_value = lambda: 42
            self.assertEqual(x.a_property(), 42)
            self.assertEqual(x.a_property(), 42)
            cm.assert_called_once()
