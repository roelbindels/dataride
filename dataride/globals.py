#!/usr/bin/env python3
""" cycling data grabber """

import http.client
import json


def getCountries():
    conn = http.client.HTTPConnection("ucibws.uci.ch")

    headers = {
        'Accept': "application/json, text/plain, */*",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Ubuntu Chromium/65.0.3325.181 \
                        Chrome/65.0.3325.181 \
                        Safari/537.36",
        'Referer': "http://ucibws.uci.ch/teamlist/en/roa",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
        'Cookie': "_ga=GA1.2.1609218398.1524685679; \
                   _gid=GA1.2.945816091.1525693560; \
                   ASPSESSIONIDCCTBATRA=FGPEOAFAHCNPMNHJMMMHPGDB; \
                   _gat=1",
        'Cache-Control': "no-cache",
        'Postman-Token': "7e8bd196-64b8-b4f1-8553-634825b4db37"
        }

    conn.request("GET", "/api/global/countries", headers=headers)

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))

    return json.dumps(parsed, indent=4, sort_keys=True)


def getContinents():
    conn = http.client.HTTPConnection("ucibws.uci.ch")

    headers = {
        'Accept': "application/json, text/plain, */*",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Ubuntu Chromium/65.0.3325.181 \
                        Chrome/65.0.3325.181 \
                        Safari/537.36",
        'Referer': "http://ucibws.uci.ch/teamlist/en/roa",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
        'Cookie': "_ga=GA1.2.1609218398.1524685679; \
                    _gid=GA1.2.945816091.1525693560; \
                    ASPSESSIONIDCCTBATRA=FGPEOAFAHCNPMNHJMMMHPGDB; \
                    _gat=1",
        'Cache-Control': "no-cache",
        'Postman-Token': "f422df3c-8d28-26b7-c96b-8667445c3a03"
        }

    conn.request("GET", "/api/global/continents", headers=headers)

    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))

    return json.dumps(parsed, indent=4, sort_keys=True)


if __name__ == '__main__':
    print(getCountries())
    print(getContinents())
