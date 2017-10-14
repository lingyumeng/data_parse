# -*- coding:utf-8 -*-

import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

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

def list_to_flost(str):
    str=str.strip()
    str=str.replace('{', '')
    str=str.replace('}', '')
    print(str)
    area_array = str.split('|')
    lengh_0 = len(area_array[0].split('e')[0])
    lengh_1 = len(area_array[1].split('e')[0])

    if lengh_0 > lengh_1:
        return float(area_array[0])
    else:
        return float(area_array[1])



def fix_area(area):
    if is_None(area):
        area = None
    elif is_float(area):
        area = float(area)
    elif is_array(area):
        area = list_to_flost(area)

    return area

def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        # skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                print(line["areaLand"])
                line["areaLand"] = fix_area(line["areaLand"])
                print(line["areaLand"])
                #print(type(line["areaLand"]))
            data.append(line)

    return data

def test():
    data = process_file(CITIES)

    print "Printing three example results"
    for n in range(5, 8):
        pprint.pprint(data[n]["areaLand"])

    assert data[3]["areaLand"] == None
    assert data[8]["areaLand"] == 55166700.0
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0

if __name__ == '__main__':
    test()
