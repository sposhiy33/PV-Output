"This script is to generate heatmaps of the Irridiance data"
import geoplot as gplt
import geoplot.crs as gcrs
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

## Contiguous US
df = gpd.read_file('CartographicBoundries/US_State/cb_2018_us_state_500k.shp')
df = df.drop([37,38,44,45,13,27,42])
contUSdf = df.dissolve()

# Load in Irridiance Data
contUS_data = pd.read_csv('Data/ContinguousUS_data.csv')
print(contUS_data)

# GeoDataFrame from the Irridaince Data
gdf_DNI = gpd.GeoDataFrame(contUS_data.AVG_dhi,
        geometry = gpd.points_from_xy(contUS_data.lon, contUS_data.lat))

##################
### PLOTS #####
##################
ax = gplt.polyplot(contUSdf, projection=gcrs.AlbersEqualArea())

gplt.pointplot(gdf_DNI, hue='AVG_dhi',
                 legend=True, ax=ax)

# gplt.kdeplot(gdf_DNI, n_levels = 100, projection=gcrs.AlbersEqualArea(), ax=ax)



# ax1 = gplt.kdeplot(
#         clip=contUSdf.geometry
#         cmap='Reds',
#         projection=gcrs.AlbersEqualArea(),
#         shade=True, shade_lowest=False,
#         clip=contUSdf.geometry,
#         ax=ax)

plt.show()
