# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

if __name__ == '__main__':
    get_root(PATENTS)