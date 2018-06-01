#!/usr/bin/env python3
""" team functions """

import http.client
import json


def get_teamridersdetail():
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/teamdetail/riders/231/1372")

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed
