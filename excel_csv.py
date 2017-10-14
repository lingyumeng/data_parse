# -*- utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
from zipfile import ZipFile

DATADIR = ""
DATAFILE = "2013_ERCOT_Hourly_Load_Data"
outfile = "2013_Max_Loads.csv"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

def parse_file(datafile):
    workbook = xlrd.open_workbook('{0}.xls'.format(datafile))
    sheet = workbook.sheet_by_index(0)
    data = None

    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to python tuple of (year, month, day, hour, minute, second)

    #filedata = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    data = []
    firstline = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
    data.append(firstline)

    areas = []
    for i in range(sheet.ncols - 1):
        areas.append(sheet.cell_value(0, i))

    print(areas)

    time_cv = sheet.col_values(0, start_rowx=1, end_rowx=None)

    for r in range(len(areas)):
        if r == 0:
            continue
        else:
            tempdata = []

            area_name = areas[r]
            tempdata.append(area_name)
            cv = sheet.col_values(r, start_rowx=1, end_rowx=None)
            cv_max = max(cv)
            max_pos = cv.index(cv_max)


            maxtime = time_cv[max_pos]
            realtime = xlrd.xldate_as_tuple(maxtime, 0)
            for j in range(len(realtime) - 2):
                tempdata.append(realtime[j])

            tempdata.append(cv_max)
            data.append(tempdata)


    return data

def save_file(data, filename):
    # YOUR CODE HERE
    with open(filename, 'wb') as f:
        csvwriter = csv.writer(f, delimiter = '|')
        for line in data:
            csvwriter.writerow(line)

def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    open_zip(datafile)
    data = parse_file(datafile)
    print(data)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

# def testparse():
#     datafile = os.path.join(DATADIR, DATAFILE)
#     open_zip(datafile)
#     data = parse_file(datafile)
#     print data
#
#     outfile = os.path.join(DATADIR, OUTFILE)
#     save_file(data, outfile)


if __name__ == '__main__':
    test()





