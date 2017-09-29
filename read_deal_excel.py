# -*- coding:utf-8 -*-

"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

please see the test funcation for the expected return format

"""
import numpy as np
import xlrd
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

def np_parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    coast_list = sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows)
    print sheet.cell_value(sheet.nrows-1, 1)
    coasts_array = np.array(coast_list)

    max_coast = coasts_array.max()
    max_index = coasts_array.argmax()

    min_coast = coasts_array.min()
    min_index = coasts_array.argmin()

    avg_coast = coasts_array.mean()
    print 'avgcoast:',
    print avg_coast

    time = sheet.cell_value(max_index+1, 0)
    max_time = xlrd.xldate_as_tuple(time, 0)
    time = sheet.cell_value(min_index+1, 0)
    min_time = xlrd.xldate_as_tuple(time, 0)

    data = {
            'maxtime': max_time,
            'maxvalue': max_coast,
            'mintime': min_time,
            'minvalue': min_coast,
            'avgcoast': avg_coast
    }

    return data

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)

    maxval = max(cv)
    minval = min(cv)

    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    realtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
        'maxtime': realtime,
        'maxvalue': maxval,
        'mintime': realmintime,
        'minvalue': minval,
        'avgcoast': sum(cv) / float(len(cv))
    }
    return data

def test():
    #open_zip(datafile)
    data = np_parse_file(datafile)
    data1 = parse_file(datafile)
    print data
    print data1
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

    assert data1['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data1['maxvalue'], 10) == round(18779.02551, 10)

if __name__ == "__main__":
    test()