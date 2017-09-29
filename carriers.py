# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

html_page = "options.html"

def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary value
        soup = BeautifulSoup(html, 'lxml')
        select_tag = soup.find(id="CarrierList")

        for carrier_tag in select_tag.find_all('option'):
            if carrier_tag.get('value') not in ("All", "AllUS", "AllForeign"):
                data.append(carrier_tag.get('value'))

    print data
    return data

def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here
        soup = BeautifulSoup(html, 'lxml')

        airportList = soup.find(id="AirportList")

        for airport in airportList.find_all('option'):
            if airport.get('value') not in ("All", "AllMajors", "AllOthers"):
                data.append(airport.get('value'))

    print data
    return data

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    s = requests.Session()

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__VIEWSTATEGENERATOR", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))

    return r.text

def test_carrier():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

def test_airport():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == '__main__':
    test_carrier()
    test_airport()

