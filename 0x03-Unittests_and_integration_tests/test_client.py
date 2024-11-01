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
            self.assertEqual(x._public_repos_url, 'pla pla pla')

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """test_public_repos
        """
        r_val = list()
        r_val.append(dict((("name", "truth"),)))
        r_val.append(dict((("name", "ruby-openid-apps-discovery"),)))
        mocked_get_json.return_value = r_val
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as m:
            m.return_value = 'https://api.github.com/orgs/google/repos'
            obj = GithubOrgClient('google')
            result = obj.public_repos()
            self.assertEqual(result, ["truth", "ruby-openid-apps-discovery"])
            m.assert_called_once()
            mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test_has_license
        """
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)
