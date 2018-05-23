#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dataride` package."""


import unittest
import json

from dataride import globals
from .support.assertions import assert_valid_schema


class TestGlobals(unittest.TestCase):
    """Tests for `dataride` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_countries(self):
        result = globals.get_countries()
        assert_valid_schema(result, 'countries.json')


    def test_get_continents(self):
        result = globals.get_continents()
        assert_valid_schema(result, 'continents.json')

