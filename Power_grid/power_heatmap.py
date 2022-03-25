import geoplot as gplt
import geoplot.crs as gcrs
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Get shape file of Continguous US
df = gpd.read_file('CartographicBoundries/US_State/cb_2018_us_state_500k.shp')
df = df.drop([37,38,44,45,13,27,42])
contUSdf = df.dissolve()

# Read in shapefile with all lines over 500kV capacity
lines = gpd.read_file("Powerlines.zip")


