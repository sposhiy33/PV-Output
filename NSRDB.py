import pandas as pd
import numpy as np
import sys, os

pd.set_option('display.max_columns', None)

# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
# Define the lat, long of the location and the year
lat,lon,year = 30.186696, -97.858323, 2020
# You must request an NSRDB api key from the link above
api_key = 'Ys1FBygszkOmc2ifUvWD8LdkRFWGaIbNByDa5Ddc'
# Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
# TO SEE OTHER VARAIBLES, https://developer.nrel.gov/docs/solar/nsrdb/himawari-download/
attributes = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle,surface_pressure,relative_humidity'
# Choose year of data
year = '2020'
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
reason_for_use = 'personal+project'
# Your affiliation
your_affiliation = 'Santa+Fe+Preparatory+School'
# Your email address
your_email = 'shreyposh@gmail.com'
# Please join our mailing list so we can keep you up-to-date on new developments.
mailing_list = 'false'

# Declare url string
url = 'https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
# Return just the first 2 lines to get metadata:
info = pd.read_csv(url)
print(info.shape)
# See metadata for specified properties, e.g., timezone and elevation
timezone, elevation = info['Local Time Zone'], info['Elevation']

info.to_csv('NSRDBout_s2.csv')
