# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.

    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    :param filename:
    :return:
    """
    n = 0
    nf = None

    with open(filename, 'r') as of:
        for line in of:
            if line.startswith("<?xml"):
                if nf:
                    nf.close()
                nf = open("{}-{}".format(filename, n), 'wb')
                n += 1

            if nf:
                nf.write(line)
    if nf:
         nf.close()



def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the file name is correct!".format(fname)

if __name__ == '__main__':
    test()
