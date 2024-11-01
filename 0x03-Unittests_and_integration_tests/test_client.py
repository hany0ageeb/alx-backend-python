#!/usr/bin/env python3
"""test_clent.py
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient
    """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org
        """
        x = GithubOrgClient(org_name)
        x.org()
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))
