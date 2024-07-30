#!/usr/bin/env python3
""" This module contains unit tests for a TestGithubOrgClient class """

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ This class contains a test for the org methode """
    @parameterized.expand([
        ("google"), ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ This methode test that the org methode return the correct value
            and that the get_json is called only once per org_name
        """
        url = f"https://api.github.com/orgs/{org_name}"
        cl = GithubOrgClient(org_name)
        cl.org()
        cl.org()
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """ Test that the _public_repos_url property returns the correct URL
        """
        payload = {
            "login": "github",
            "url": "https://api.github.com/orgs/github",
            "repos_url": "https://api.github.com/orgs/github/repos",
            "events_url": "https://api.github.com/orgs/github/events",
        }
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock:
            mock.return_value = payload
            cls = GithubOrgClient("github")
            self.assertEqual(cls._public_repos_url,
                             "https://api.github.com/orgs/github/repos")
