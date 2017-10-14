# -*- coding:utf-8 -*-

import codecs
import csv
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

def fix_name(name):
    if is_None(name):
        name = []
    elif is_array(name):
        name = name.strip()
        name = name.replace('{', '')
        name = name.replace('}', '')
        name = name.split('|')
    else:
        name = [name]

    return name

def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)

    return data

def test():
    data = process_file(CITIES)

    print("Printing 20 results:")
    for n in range(20):
        pprint.pprint(data[n]["name"])

    assert data[14]["name"] == ['Negtemiut', 'Nightmute']
    assert data[9]["name"] == ['Pell City Alabama']
    assert data[3]["name"] == ['Kumhari']


if __name__ == '__main__':
    test()
