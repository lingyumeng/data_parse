# -*- utf-8 -*-

"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query paramenters are given to the requests.get function as a dictionary;
# This variable contains some starter paramenters.

query_type = { "simple": {},
               "atr": {"inc":"aliases+tags+ratings"},
               "aliases": {"inc": "aliases"},
               "releases": {"inc": "releases"}}

def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    :param url:
    :param params:
    :param uid:
    :param fmt:
    :return:
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

def query_by_name(url, parsms, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    :param url:
    :param parsms:
    :param name:
    :return:
    """
    parsms["query"] = "artist:" + name
    return query_site(url, parsms)

def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    :param data:
    :param indent:
    :return:
    """
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data

def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    pretty_print(results)

    # Isolate infoemation from the 4th band returned (index 3)
    print "\nARTIST:"
    pretty_print(results["artists"][3])

    # Query for releases from that band using the artist_id
    artist_id = results["artists"][3]["id"]
    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]

    # Print information about releases from the selected band
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)

    release_titles = [r["title"] for r in releases]
    print  "\nALL TITLES:"
    for t in release_titles:
        print t

def count_by_name(name=""):
    # Query for information in the database about bands named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], name)
    pretty_print(results)
    band_list = results["artists"]

    count = 0
    for artist in band_list:
        if artist["name"] == name:
            count += 1
    print "list count:", count

def search_begin_area(name):
    result = query_by_name(ARTIST_URL, query_type["simple"], name)
    #pretty_print(result)
    begin_area = result["artists"][2]["begin-area"]["name"]
    print begin_area

def find_alias(name):
    band_result = query_by_name(ARTIST_URL, query_type["simple"], name)
    #pretty_print(band_result)
    alias = band_result["artists"][0]["aliases"][8]["name"]
    print alias

def find_dis(name):
    band_n = query_by_name(ARTIST_URL, query_type["simple"], name)
    #pretty_print(band_n)
    print band_n["artists"][4]['disambiguation']

def find_begin_time(name):
    band_result = query_by_name(ARTIST_URL, query_type["simple"], name)
    #pretty_print(band_result)
    print band_result["artists"][0]["life-span"]["begin"]

if __name__ == '__main__':
    #main()
    count_by_name("First Aid Kit")
    search_begin_area("Queen")
    find_alias("The Beatles")
    find_dis("Nirvana")
    find_begin_time("One Direction")
