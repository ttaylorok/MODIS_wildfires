from geojson import Polygon, Point, Feature, FeatureCollection
import folium
import pandas as pd
from scipy.spatial import ConvexHull, convex_hull_plot_2d

import sys
from descartes import PolygonPatch
import matplotlib.pyplot as plt
import alphashape

# load data and filter out unclassified points
df = pd.read_csv("class_output.csv")
df = df[df["optic_class"] != -1]
df = df[(df["optic_class"] == 53) |
        (df["optic_class"] == 68) |
        (df["optic_class"] == 35) |
        (df["optic_class"] == 67) |
        (df["optic_class"] == 31) |
        (df["optic_class"] == 62) |
        (df["optic_class"] == 15) |
        (df["optic_class"] == 44) |
        (df["optic_class"] == 18) |
        (df["optic_class"] == 14) |
        (df["optic_class"] == 13) |
        (df["optic_class"] == 5)  |
        (df["optic_class"] == 12) |
        (df["optic_class"] == 42) |
        (df["optic_class"] == 56) |
        (df["optic_class"] == 24) |
        (df["optic_class"] == 31) |
        (df["optic_class"] == 32) |
        (df["optic_class"] == 61)]
df.set_index(keys="optic_class", inplace=True)

m = folium.Map([38.2,-118.6], zoom_start=6)
features = []
for x in df.index.unique():
    print(x)
    # calculate convex hull of optic esclass
    points = df.loc[x,["lon","lat"]].to_numpy()
    #hull = ConvexHull(points)
    hull = alphashape.alphashape(points, 50)
       
    # calculate acreage of fire
    size = df.loc[x,"date"].count()*926.625*926.625*0.000247105
    
    d = df.loc[x,"date"].mode()
    print(d[0])
 
    # poly = []
    # for y in hull.vertices:
    #     poly.append((points[y,1],points[y,0]))
    
    f = Feature(geometry = hull,
                properties = {"date" : d[0], "acres" : int(size)})
    features.append(f)
    
    

style = {'fillColor': '#d41414', 'fillOpacity': 0.5, 'color' : '#d41414', 'weight' : 2}
styleh = {'fillColor': '#d41414', 'fillOpacity': 0.5, 'color' : '#d41414', 'weight' : 4}

# add JSON object to map
folium.GeoJson(
    FeatureCollection(features),
    tooltip=folium.features.GeoJsonTooltip(fields=['date','acres'],labels=True), 
    style_function = lambda x : style,
    highlight_function = lambda x : styleh,
    name='poly_layer'   
).add_to(m)

m.save('chloro_test_full_alpha3.html')

    
