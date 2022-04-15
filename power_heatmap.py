import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries
import geoplot
import shapely
import shapely.speedups
import matplotlib.pyplot as plt
import math
import numpy

pd.set_option('display.max_columns', None)
shapely.speedups.enable()

# Get shape file of Continguous US
df = gpd.read_file('CartographicBoundries/US_State/cb_2018_us_state_500k.shp')
df = df.drop([37,38,44,45,13,27,42])
contUSdf = df.dissolve()
ax = contUSdf.plot(color='white', edgecolor='black')

bound = pd.DataFrame(contUSdf.bounds)

# Read in shapefile with all lines over 500kV capacity
lines = gpd.read_file("Powerlines.zip")

power = shapely.ops.unary_union(lines['geometry'])

def main():

    l_bounds = list(find_boundary(0))
    num_of_div = list(num_of_divisions(5000))
    len_of_each_div = list(len_of_div(l_bounds, num_of_div[0], num_of_div[1]))

    coords = coord_of_div(len_of_each_div, l_bounds, num_of_div)
    lat = coords[1]
    lon = coords[0]

    points = point_dataframe(lon, lat)
    print(points)

    distance = dist(points, power)
    print(distance)

    points.plot(ax=ax, color='red')
    plt.show()

# Return a list of the boundries from the Polygon

def find_boundary(index):

    minx = bound.iat[index, 0]
    miny = bound.iat[index, 1]
    maxx = bound.iat[index, 2]
    maxy = bound.iat[index, 3]

    return minx, miny, maxx, maxy

def multiples(n):
    l = [*range(1, n+1)]
    multiples = []
    for i in range(1, l[len(l)-1]+1):
        if n % i == 0:
            multiples.append(i)

    return multiples


# Find the number of subdivisions to make,
# Uses the middle 2 elements of the mutiples list ...
# ... (created by above function)
def num_of_divisions(area):
    m = multiples(area)
    w_n = m[len(m) // 2]
    h_n = m[len(m) // 2]
    if (len(m) % 2) == 1:
        return w_n, h_n
    else:
        h_n = m[(len(m) // 2) - 1]
    return w_n, h_n

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



def point_dataframe(longitude, latitude):

    point = pd.DataFrame(columns = ['lon', 'lat'])
    for x in longitude:
        for y in latitude:
            point2 = pd.DataFrame([{'lon':x, 'lat':y}])
            point = point.append(point2, ignore_index = True)

    gdf = gpd.GeoDataFrame(point,
            geometry = gpd.points_from_xy(point.lon, point.lat))

    ## Check if point is in main polygon
    # pip = 'point in polygon'

    pip_mask = gdf.within(contUSdf.loc[0, 'geometry'])
    pip_data = gdf.loc[pip_mask]

    return pip_data

def min_dist(point, gpd2):
    gpd2['Dist'] = gpd2.apply(lambda row:  point.distance(row.geometry),axis=1)
    return gpd2

def get_geom(row):
    geom = row.geometry
    print(type(geom))
    return geom

def dist(point, linestring):
    dists = []
    for row in range(len(point)):
        each_point = get_geom(point[row])
        distance = shapely.ops.nearest_points(each_point, linestring)
        dists.append(distance)
    return dists


def min_distance(point, line):
    print(type(point['geometry']))
    distance = point.geometry.apply(shapely.ops.nearest_points(point, line))
    return distance



main()