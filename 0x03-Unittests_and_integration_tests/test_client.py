#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


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
        mock_get_json.return_value = {"org_url": url}
        cl = GithubOrgClient(org_name)
        res = cl.org
        self.assertEqual(res, {"org_url": url})
        mock_get_json.assert_called_once_with(url)
