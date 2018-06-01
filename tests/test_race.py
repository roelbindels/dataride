#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dataride` package."""


import unittest
import json

from dataride import race
from .support.assertions import assert_valid_schema


class TestRace(unittest.TestCase):
    """Tests for `dataride` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_competitions(self):
        # print(get_countries())
        disciplineId = 10
        filterdict = {'filter' : []}
        filterdict['filter'].append({'field' : 'RaceTypeId', 'value' : 0})
        filterdict['filter'].append({'field' : 'CategoryId', 'value' : 0})
        filterdict['filter'].append({'field' : 'SeasonId', 'value' : 89})
        page = 1
        pageSize = 40
        skip = 0
        sort = [{'dir' : 'desc', 'field' : 'StartDate'}]
        take = 40

        result = race.get_competitions(disciplineId, filterdict, page, pageSize,
                                       skip, sort, take)
        assert_valid_schema(result, 'competitions.json')


    def test_get_results(self):
        result = race.get_results(1,40,155021,10)
        assert_valid_schema(result, 'results.json')

