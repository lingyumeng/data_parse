# -*- coding:utf-8 -*-
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS =  ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = {}

    # YOUR CODE HERE

    return fieldtypes

def test():
    fieldtypes = audit_file(CITIES, FIELDS)
    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes["areaMetro"] == set([type(1.1), type(None)])

if __name__ == '__main__':
    test()
