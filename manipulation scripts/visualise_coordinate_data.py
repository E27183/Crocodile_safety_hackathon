from matplotlib import pyplot as pyp
import pandas as pd

data = pd.read_excel("../data/Crocodile_Survey_Data_2021_22.xlsx", "Cleaned data")

scatter = pyp.scatter(data["Longitude"], data["Latitude__"], s=0.1, alpha=1)
pyp.show()