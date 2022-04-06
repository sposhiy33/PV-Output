"This script is to generate heatmaps of the Irridiance data"
import geoplot as gplt
import geoplot.crs as gcrs
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

## Contiguous US
df = gpd.read_file('CartographicBoundries/US_State/cb_2018_us_state_500k.shp')
contUSdf = df.drop([37,38,44,45,13,27,42])
contUSdf = contUSdf.dissolve()

# Load in Irridiance Data
data = pd.read_csv('FinalOutData.csv')

# GeoDataFrame from the Irridaince Data
# predData = gpd.GeoDataFrame(data['Predicted Generation'],
#         geometry = gpd.points_from_xy(data.lon, data.lat))

# sites = gpd.GeoDataFrame(geometry=gpd.points_from_xy([-97.86,-116.94], [30.17,32.85]))

maximum = gpd.GeoDataFrame(geometry=gpd.points_from_xy([-115.802026], [33.10023]))

##################
### PLOTS #####
##################
ax = contUSdf.plot(color='white',edgecolor='black')

# gplt.pointplot(maximum,ax=ax,extent=contUSdf.total_bounds)


maximum.plot(ax=ax, c='r', markersize = 60)

# gplt.pointplot(predData, hue='Predicted Generation',
#                  legend=True, ax=ax)

plt.title("Most Optimal Location for PV Panel in Contiguous US")





plt.show()
