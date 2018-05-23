#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dataride` package."""


import unittest
import json

from dataride import teams
from .support.assertions import assert_valid_schema


class TestTeams(unittest.TestCase):
    """Tests for `dataride` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_teamlist(self):
        result = teams.get_teamlist(2018)
        assert_valid_schema(result, 'teams.json')

    def test_get_teamroles(self):
        result = teams.get_teamroles()
        assert_valid_schema(result, 'teamroles.json')

    def test_get_teamcategories(self):
        result = teams.get_teamcategories(2018)
        assert_valid_schema(result, 'teamcategories.json')

