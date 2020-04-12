import folium
from folium import plugins
import pandas as pd
import numpy as np
from ipywidgets import interact
import ipywidgets as widgets
import datetime
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, OPTICS,cluster_optics_dbscan
import pandas as pd
import numpy as np

data = pd.read_csv("cali_2018_fires_output.csv", index_col="date", parse_dates=True)
data.sort_index(inplace=True)
#dates = data.index

X = data.loc[:,["lat","lon"]].to_numpy()
Y = data.loc[:,["X","Y"]].to_numpy()

y_pred_kmeans = KMeans(n_clusters=30).fit_predict(Y)

plt.scatter(Y[:, 0], Y[:, 1], c=y_pred_kmeans)
plt.show()

clustm1 = OPTICS(min_samples=70, max_eps=10000, xi=0.4)
clustm1.fit(Y)

fig = plt.figure(figsize=[12,12])
plt.scatter(Y[:, 0], Y[:, 1], c=clustm1.labels_)
plt.gca().invert_yaxis()
fig.savefig("figout")
plt.show()

data['optic_class']=clustm1.labels_
data['kmns_class']=y_pred_kmeans

data.to_csv("class_output.csv")





