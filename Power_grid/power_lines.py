import geoplot as gplt
import geoplot.crs as gcrs
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Contiguous US
df = gpd.read_file('CartographicBoundries/US_State/cb_2018_us_state_500k.shp')
df = df.drop([37,38,44,45,13,27,42])
contUSdf_unprojected = df.dissolve()
contUSdf = contUSdf_unprojected.to_crs('EPSG:5070')

# Load all transmission line datasets
power = gpd.read_file("Electric_Power_Transmission_Lines.zip")

# Remove all transmission lines with less than 500kV capacity
kV500 = power.drop(power.index[power['VOLTAGE'] < 500])
print(type(kV500))

# Create a new shapefile with only lines over 500kV
kV500.to_file('Powerlines.shp')

# Set projection of data (Using AlbersEqualArea?)
gdf_power = kV500.to_crs('EPSG:5070')

##################
### PLOTS #####
##################
final = gdf_power.clip(contUSdf)

final.plot()
plt.show()