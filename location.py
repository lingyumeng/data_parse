# -*- coding:utf-8 -*-

import csv
import pprint

CITIES = 'cities.csv'

def check_loc(point, lat, longi):
    # CODE
    point = point.strip()
    arraypoint = point.split(' ')

    if arraypoint[0] == lat.strip() and arraypoint[1] == longi.strip():
        return True
    else:
        return False


def process_file(filename):
    data = []

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        for i in range(3):
            l = reader.next()

        for line in reader:
            result = check_loc(line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"])
            if not result:
                print("{}: {} != {} {}".format(line["name"], line["point"], line["wgs84_pos#lat"], line["wgs84_pos#long"]))
            data.append(line)

    return data

def test():
    assert check_loc("33.08 75.28", "33.08", "75.28") == True
    assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") == False

if __name__ == '__main__':
    test()
