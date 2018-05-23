#!/usr/bin/env python3
""" team functions """

import http.client
import json


def get_teamroles():
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/teamsettings/seasonfunctions/roa")

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


def get_teamlist(year, teamtype='roa'):
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/teamlist/0/{}/{}".format(teamtype, year))

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


def get_teamcategories(year, teamtype='roa'):
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/teamsettings/teamcategories/{}/{}".format(teamtype, year))

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


if __name__ == '__main__':
    # print(get_teamroles())
    print(get_teamcategories(2018))
