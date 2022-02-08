import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries
import matplotlib.pyplot as plt
import math


# pd.set_option('display.max_columns', None)

# Read file
df = gpd.read_file('USAStateBorderGIS/cb_2018_us_state_500k.shp')
# This segment makes a new data table with the lower and upper bounds of each state
# Format of bounds = minx , miny , maxx , maxy
GeoDF = gpd.GeoDataFrame(df)
bound = pd.DataFrame(GeoDF.bounds)

def main():
    # NOTE: index of CO = 21
    list_of_bounds = list(boundary(21))
    num_of_div = list((num_of_divisions(500)))
    len_of_each_div = list(len_of_div(list_of_bounds, num_of_div[0], num_of_div[1]))

    # List of coords to use for the data base
    # coords[0] = the coords of the widths
    # coords[1] = the coords of the heights
    coords = coord_of_div(len_of_each_div, list_of_bounds, num_of_div)

    data = get_data(coords[1], coords[0])
    print(data)
    data.to_csv("testdata.csv")

# Returns the boundries of state
def boundary(state_index):

    minx = bound.iat[state_index, 0]
    miny = bound.iat[state_index, 1]
    maxx = bound.iat[state_index, 2]
    maxy = bound.iat[state_index, 3]

    return minx, miny, maxx, maxy

# All multiples of a given number
def multiples(n):
    l = [*range(1, n+1)]
    multiples = []
    for i in range(1, l[len(l)-1]+1):
        if n % i == 0:
            multiples.append(i)

    return multiples

# Will decide number of subdivsions to equal the total area (subdivisions of width are given first)
### COME BACK AND REVIEW: need to be able to make this part universal to any list
# ------- I fixed this, but it assumes that we want the grid to look like a square and have the width as the larger value
def num_of_divisions(area):
    m = multiples(area)
    w_n = m[len(m) // 2]
    h_n = m[len(m) // 2]
    if (len(m) % 2) == 1:
        return w_n, h_n
    else:
        h_n = m[(len(m) // 2) - 1]
    return w_n, h_n

# Gives us the coordinate length of each div (again, length of each div along the width is given first)
def len_of_div(bounds, width_n, height_n):
    a = bounds[0]

    # width subdivision
    width = bounds[2] - bounds[0]
    length_of_each_div_w = width/width_n

    # length subdivision
    height = bounds[3] - bounds[1]
    length_of_each_div_h = height/height_n

    return length_of_each_div_w, length_of_each_div_h

def coord_of_div(len_div, bounds, num_of_divs):

    ## formula for first point = a + (1/2)length
    initial_coord_w = bounds[0] + (0.5 * len_div[0])
    initial_coord_h = bounds[1] + (0.5 * len_div[1])

    w = []
    h = []

    for i in range (num_of_divs[0]):
        w.append(initial_coord_w + (i * len_div[0]))

    for i in range (num_of_divs[1]):
        h.append(initial_coord_h + (i * len_div[1]))

    return w, h

# Get the average value of a column of numerical data
def get_avg_col(data, col, starting_row, index_num_of_last_row, number_of_rows):

    total = 0

    for i in range(starting_row, index_num_of_last_row + 1):
        z = int(data.iloc[i,col])
        total = total + z

    avg = total/number_of_rows

    return avg



## ACTUALLY GETTING THE DATA FROM THE NSRDB API
def get_data(list_height, list_width):

    df = pd.DataFrame(columns = ['lata', 'long', 'AVG_ghi', 'AVG_dhi', 'AVG_dni'])

    for latitude in list_height:
        for longitude in list_width:
            # Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
            # Define the lat, long of the location and the year
            lat,lon,year = latitude, longitude, 2020
            # You must request an NSRDB api key from the link above
            api_key = 'Ys1FBygszkOmc2ifUvWD8LdkRFWGaIbNByDa5Ddc'
            # Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
            attributes = 'ghi,dhi,dni'
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
            # See metadata for specified properties, e.g., timezone and elevation
            timezone, elevation = info['Local Time Zone'], info['Elevation']

            avg_ghi = get_avg_col(info, 5, 2, 8761, 8760)
            avg_dhi = get_avg_col(info, 6, 2, 8761, 8760)
            avg_dni = get_avg_col(info, 7, 2, 8761, 8760)

            df2 = pd.DataFrame([{'lata':latitude, 'long':longitude, 'AVG_ghi':avg_ghi, 'AVG_dhi':avg_dhi, 'AVG_dni':avg_dni}])
            df = df.append(df2, ignore_index = True)

    return(df)

main()
