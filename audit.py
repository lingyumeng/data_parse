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

def is_None(str):
    if str == "NULL" or str == "":
        return True
    elif str is None:
        return True
    else:
        return False
def is_array(str):
    str = str.strip()
    if str.startswith("{"):
        return True
    else:
        return False

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_float(str):
    try:
        float(str)
        if is_int(str):
            return False
        else:
            return True
    except ValueError:
        return False


def audit_file(filename, fields):
    fieldtypes = {}

    for key in fields:
        fieldtypes[key] = set()


    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for i in range(3):
            reader.next()


        for row in reader:
            for clomunname in FIELDS:
                #print(row[clomunname])
                if is_None(row[clomunname]):
                    fieldtypes[clomunname].add(type(None))
                elif is_array(row[clomunname]):
                    fieldtypes[clomunname].add(type([]))
                elif is_float(row[clomunname]):
                    fieldtypes[clomunname].add(type(1.1))
                elif is_int(row[clomunname]):
                    fieldtypes[clomunname].add(type(1))
                else:
                    fieldtypes[clomunname].add(type("string"))

    return fieldtypes

def test():
    fieldtypes = audit_file(CITIES, FIELDS)
    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes["areaMetro"] == set([type(1.1), type(None)])

if __name__ == '__main__':
    test()
