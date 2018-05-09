#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dataride` package."""


import unittest

from dataride import globals


class TestDataride(unittest.TestCase):
    """Tests for `dataride` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        self.assertNotEqual(globals.getCountries(), "")
        self.assertNotEqual(globals.getContinents(), "")
