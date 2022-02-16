from multiprocessing import BoundedSemaphore
import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries
import matplotlib.pyplot as plt
import math
import fiona

# Read file
df = gpd.read_file('USAStateBorderGIS/cb_2018_us_nation_5m.zip')
# This segment makes a new data table with the lower and upper bounds of each state
# Format of bounds = minx , miny , maxx , maxy
GeoDF = gpd.GeoDataFrame(df)
GeoDF = GeoDF.to_crs("EPSG:3395")
ContGeoDF = GeoDF.explode()
bound = pd.DataFrame(GeoDF.bounds)

#def find_US(data, start, finish):
    #for i in range(start, finish + 1):


def get_Island_area(data, row_number):
    all_polygons_gdf = gpd.GeoDataFrame(data)
    row = all_polygons_gdf.iloc[row_number]
    shape = data.iat[row_number, 3]
    gdf = gpd.GeoDataFrame({'data' : [row], 'geometry' : [shape]})
    area = gdf.area

    return area



def get_DataFrame_row(data, row_number):
    all_polygons_gdf = gpd.GeoDataFrame(data)
    row = all_polygons_gdf.iloc[row_number]
    shape = data.iat[row_number, 3]
    gdf = gpd.GeoDataFrame({'data' : [row], 'geometry' : [shape]})

    return gdf

for i in range(0, 290):
    area = get_Island_area(ContGeoDF, i)
    #print(i, area)

usa = get_DataFrame_row(ContGeoDF, 146)
print(type(usa))
#usa.to_file('Cont_US.shp')

usa.plot()
plt.show()
