import http.client
import json


def get_disciplines():
    conn = http.client.HTTPConnection("ucibws.uci.ch")
    conn.request("GET", "/api/global/disciplines")
    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


def _get_filterstring(filterdict):
    result = ""
    for index, filteritem in enumerate(filterdict['filter']):
        for field, value in filteritem.items():
            result = result + \
                        "filter[filters][{}][{}]={}&" \
                        .format(index, field, value)
    return result


def _get_sortstring(sortdict):
    result = ""
    for index, item in enumerate(sortdict):
        for field, value in item.items():
            result = result + \
                        "sort[{}][{}]={}&" \
                        .format(index, field, value)
    return result


def get_competitions(disciplineId, filterdict, page, pageSize,
                     skip, sortdict, take):
    conn = http.client.HTTPSConnection("dataride.uci.ch")
    payload = _get_filterstring(filterdict) + \
        _get_sortstring(sortdict) + \
        ("disciplineId={}&"
         "page={}&"
         "pageSize={}&"
         "skip={}&"
         "take={}").format(disciplineId,
                           page, pageSize, skip,
                           take)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
        }
    conn.request("POST", "/iframe/Competitions/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed


def get_results(page, pageSize, eventId, disciplineId):
    conn = http.client.HTTPSConnection("dataride.uci.ch")
    payload = "page={}&pageSize={}&eventId={}&disciplineId={}". \
              format(page, pageSize, eventId, disciplineId)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        }
    conn.request("POST", "/iframe/Results/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    parsed = json.loads(data.decode("utf-8"))
    return parsed
