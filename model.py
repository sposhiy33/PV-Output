import pandas as pd
import matplotlib as mb
import numpy as np
import sys, os
from IPython.display import display

# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
# Define the lat, long of the location and the year
lat, lon, year = 33.2164, -97.1292, 2010
# You must request an NSRDB api key from the link above
api_key = 'KJLAhPJpHhvfJ4UXGkssJSwWpr0fBdn24Kv6HHNw'
# Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
attributes = 'dhi,dni,air_temperature'
# Choose year of data
year = '2010'
# Set leap year to true or false. True will return leap day data if present, false will not.
leap_year = 'false'
# Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
interval = '60'
# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
# local time zone.
utc = 'true'
# Your full name, use '+' instead of spaces.
your_name = 'Shrey+Poshiya'
# Your reason for using the NSRDB.
reason_for_use = 'Personal+Project'
# Your affiliation
your_affiliation = 'Santa+Fe+Peraratory+School'
# Your email address
your_email = 'shreyposh@gmail.com'
# Please join our mailing list so we can keep you up-to-date on new developments.
mailing_list = 'false'
# Declare url string
url = 'https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
# Return just the first 2 lines to get metadata:
info = pd.read_csv(url, nrows=100)
# See metadata for specified properties, e.g., timezone and elevation
timezone, elevation = info['Local Time Zone'], info['Elevation']

# Return all but first 2 lines of csv to get data:
df = pd.read_csv(url)
print(df.head(2)) 