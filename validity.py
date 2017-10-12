# -*- coding:utf-8 -*-

"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""

import csv
import time
#import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    g_list = []
    b_list = []

    def is_date(datestr):
        try:
            time.strptime(datestr, '%Y-%m-%d')
            return True
        except:
            return False



    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        while True:
            try:
                line = reader.next()
                if line['URI'].find("dbpedia.org") < 0:
                    continue

                datestr = line['productionStartYear'][:10]
                print datestr

                if is_date(datestr):
                    if int(datestr[:4]) > 1886 and int(datestr[:4]) < 2004:
                        line['productionStartYear'] = time.strptime(datestr[:4], '%Y').tm_year
                        print(line['productionStartYear'])
                        g_list.append(line)
                    else:
                        b_list.append(line)
                else:
                    b_list.append(line)

            except:
                break

        # COMPLETE THIS FUNCTION
    print len(g_list)
    print len(b_list)

    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, 'w') as g:
        writer = csv.DictWriter(g, delimiter=',', fieldnames=header)
        writer.writeheader()
        for row in g_list:
            writer.writerow(row)

    with open(output_bad, 'w') as b:
        bwriter = csv.DictWriter(b, delimiter=',', fieldnames=header)
        bwriter.writeheader()
        for brow in b_list:
            bwriter.writerow(brow)

def test():
    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)

if __name__ == '__main__':
    test()