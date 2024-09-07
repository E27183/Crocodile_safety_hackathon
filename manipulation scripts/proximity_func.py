#Step 1 -> cluster data (if a thing)
#Step 2 -> model data clusters by time and distance
#Step 3 -> make predictions

import pandas as pd
from sklearn.cluster import AgglomerativeClustering as km
from sklearn.model_selection import train_test_split as spl
import numpy as np

data = pd.read_excel("../data/Crocodile_Survey_Data_2021_22.xlsx", "Cleaned data")
latitude = data["Latitude__"].to_numpy()
longitude = data["Longitude"].to_numpy()
time = data["UTC_Date"].dt.year.to_numpy()
time = time - time.min()

# data_array = np.stack((latitude, longitude), axis=1)
# data_array = data_array.T
# data_array[0] *= data_array.shape[0] / (data_array[0] @ data_array[0].T)
# data_array[1] *= data_array.shape[0] / (data_array[1] @ data_array[0].T)
# data_array = data_array.T
# #data_array[2] *= data_array.shape[0] / (data_array[2] @ data_array[0].T)

# train, split = spl(data_array, test_size=0.3)
# test, valid = spl(split, test_size=0.5)
# kmeans = km(n_clusters=9)
# kmeans.fit(train)
# labels = kmeans.labels_

from matplotlib import pyplot as pyp
# trainT = train.T
scatter = pyp.scatter(latitude, longitude, c=time, s=0.1, alpha=1)
scatter.set_aspect('equal', adjustable='box')

pyp.show()
