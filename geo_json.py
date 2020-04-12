from geojson import Polygon, Point, Feature
import folium
import pandas as pd
from scipy.spatial import ConvexHull, convex_hull_plot_2d

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
for x in df.index:
    # calculate convex hull of optic esclass
    points = df.loc[x,["lat","lon"]].to_numpy()
    hull = ConvexHull(points)
       
    # calculate acreage of fire
    size = df.loc[x,"date"].count()*926.625*926.625*0.000247105
 
    poly = []
    for y in hull.vertices:
        poly.append((points[y,1],points[y,0]))
    
    # add JSON object to map
    folium.GeoJson(
        Polygon([poly]),
        name='geojson',
        tooltip="class: %d, size: %.0f acres" % (x,size),
    ).add_to(m)

m.save('chloro_test_2.html')

    
