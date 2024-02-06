#!/usr/bin/env python3
''' unittest '''
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    ''' class '''
    def test_org(self):
