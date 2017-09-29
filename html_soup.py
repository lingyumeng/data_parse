# -*- coding:utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function

from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"

def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, 'r') as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, 'lxml')
        for input_tag in soup.find_all('input'):
            print input_tag
            if input_tag.get('id') == "__EVENTVALIDATION":
                data["eventvalidation"] = input_tag['value']
            elif input_tag.get('id') == "__VIEWSTATE":
                data["viewstate"] = input_tag['value']
            else:
                continue

    return data

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                      data={'AirportList': "BOS",
                            'CarrierList': "VX",
                            'Submit': 'Submit',
                            "__EVENTTARGET": "",
                            "__EVENTARGUMENT": "",
                            "__EVENTVALIDATION": eventvalidation,
                            "__VIEWSTATE": viewstate
                            })

    return r.text

def test():
    data = extract_data(html_page)
    #print data
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")

if __name__ == '__main__':
    test()

