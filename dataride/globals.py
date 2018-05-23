#!/usr/bin/env python3
""" cycling data grabber """

import http.client
import json


def get_countries():
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/global/countries")

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


def get_continents():
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/global/continents")

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


if __name__ == '__main__':
    print(get_countries())
    print(get_continents())
