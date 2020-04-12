import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


m = folium.Map([41.6583,-122.1131], zoom_start=11)

data = [[41.6667, -122.1177, 8.00],
        [41.6583, -122.1131, 8.00],
        [41.6583, -122.1019, 9.00]]

data = pd.read_csv("cali_2018_fires_output.csv")

latlongs = data[["lat","lon"]]

# for index, row in enumerate(data):
#     folium.CircleMarker([row[0], row[1]],
#                         radius=15,
#                         popup=row[2],
#                         fill_color="#3db7e4", # divvy color
#                        ).add_to(m)
    
# convert to (n, 2) nd-array format for heatmap
stationArr = latlongs.to_numpy()

# plot heatmap
m.add_child(plugins.HeatMap(stationArr, radius=15))
#m


m.save('map_test.html')