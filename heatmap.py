import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

geodf = gpd.read_file('USAStateBorderGIS/cb_2018_us_state_500k.shp')
df = pd.read_csv('Irridiance_Colorado.csv')
