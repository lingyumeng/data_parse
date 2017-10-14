# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"

def open_zip(datadir):
    if os.path.isfile('{0}.zip'.format(datadir)):
        with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
            myzip.extractall()

def process_all(datadir):
    files = os.listdir(datadir)
    return files

def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    :param f:
    :return:
    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]

    """
    data = []

    with open("{}/{}".format(datadir, f), "r") as html:
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find(id="DataGrid1")
        for dataTDRight in table.find_all("tr", attrs={"class": "dataTDRight"}):
        #for dataTDRight in table.select("tr.dataTDRight"):
            if not dataTDRight.find("b"):
                info = {}
                info["courier"], info["airport"] = f[:6].split('-')
                df = dict()
                dataflights = list(dataTDRight.children)
                info["year"] = int(dataflights[1].get_text().encode())
                info["month"] = int(dataflights[2].get_text().encode())
                print(info["month"])
                df["domestic"] = int(dataflights[3].get_text().encode().replace(',', ''))
                df["international"] = int(dataflights[4].get_text().encode().replace(',', ''))
                info["flights"] = df

                print(info)
                data.append(info)
                print(data[0])

    return data

def test():
    print("Running a simple test...")
    open_zip(datadir)
    files = process_all(datadir)
    data = []

    # Test will loop over three data files.
    for f in files:
        data += process_file(f)

    #assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    #assert data[-1]["airport"] == "ATL"
    #assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}

    #print data
    print("... success!")

if __name__ == '__main__':
    test()
