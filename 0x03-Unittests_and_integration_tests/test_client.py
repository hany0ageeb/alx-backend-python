#!/usr/bin/env python3
"""test_clent.py
"""
import unittest
import unittest.mock
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """test_public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = dict({'repos_url': 'pla pla pla'})
            x = GithubOrgClient('google')
            # print(x.org)
            self.assertEqual(x._public_repos_url, 'pla pla pla')
