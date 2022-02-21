"This script is to generate heatmaps of the Irridiance data"
import pandas as pd
import geopandas
# import geoplot.crs as gcrs
import matplotlib.pyplot as plt
import math

pd.set_option('display.max_columns', None)


## get shapefile of the US states and plot
states = geopandas.read_file('CartographicBoundries/US_State/cb_2018_us_state_500k.shp')

# Colorado index = 21
state_index = 21
state_row = states.iloc[[state_index]]


## make geodataframe from the irridiance data that was collected
## from 'data.py'
irridiance = pd.read_csv("Irridiance_Colorado.csv")

gdf = geopandas.GeoDataFrame(irridiance,
        geometry = geopandas.points_from_xy(irridiance.long, irridiance.lata))


## And now ... plot everything ##

ax1 = state_row.plot(color='white', edgecolor='black')
gdf.plot(ax=ax1, color='red')
plt.show()
