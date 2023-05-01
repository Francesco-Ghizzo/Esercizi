import collections
import csv
import datetime
import sys

import requests

stations = sys.argv[1].split(",")
years = [int(year) for year in sys.argv[2].split("-")]
start_year = years[0]
start_year = years[1]

TEMPLATE_URL = "https://www.ncei.noaa.gov/data/global-hourly/access/{year}/{station}.csv"
TEMPLATE_FILE = "station_{station}_{year}.csv"

def download_data(station, year):
    my_url = TEMPLATE_URL.format(station=station, year=year)
    req = requests.get(my_url)
    if req.status_code != 200:
        return # not found
    w = open(TEMPLATE_FILE.format(station=station, year=year), "wt") w.write(req.text)
    w.close()

def download_all_data(stations, start_year, end_year): for station in stations:
    for year in range(start_year, end_year + 1):
        download_data(station, year)
