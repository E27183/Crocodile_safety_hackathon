from sklearn.ensemble import RandomForestRegressor as forest
# from sklearn.linear_model import LogisticRegression as forest
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

dp = "../data/"

h = 0
t = 60
yr = 2023
m = 1

darw_model = forest(n_estimators = 500)
kath_model = forest(n_estimators = 500)
nhul_model = forest(n_estimators = 500)
borr_model = forest(n_estimators = 500)

darw_data = pd.read_csv(dp+"Darwin_ml_data.csv")
darw_data = darw_data[darw_data["Temp"] != -10][darw_data["Water level"] != -10]

y = darw_data[["Crocs"]].to_numpy()
x = darw_data[["Water level", "Temp", "Year", "Month"]].to_numpy()

darw_model.fit(x, y.reshape(-1, 1))
print(darw_model.predict([[h, t, yr, m]]))

kath_data = pd.read_csv(dp+"Katherine_ml_data.csv")
kath_data = kath_data[kath_data["Temp"] != -10][kath_data["Water level"] != -10]

y = kath_data[["Crocs"]].to_numpy()
x = kath_data[["Water level", "Temp", "Year", "Month"]].to_numpy()

kath_model.fit(x, y.reshape(-1, 1))
print(kath_model.predict([[h, t, yr, m]]))

nhul_data = pd.read_csv(dp+"Nhulunbuy_ml_data.csv")
nhul_data = nhul_data[nhul_data["Temp"] != -10]

y = nhul_data[["Crocs"]].to_numpy()
x = nhul_data[["Temp", "Year", "Month"]].to_numpy()

nhul_model.fit(x, y.reshape(-1, 1))
print(nhul_model.predict([[t, yr, m]]))

borr_data = pd.read_csv(dp+"Borroloola_ml_data.csv")
borr_data = borr_data[borr_data["Temp"] != -10][borr_data["Water level"] != -10]

y = borr_data[["Crocs"]].to_numpy()
x = borr_data[["Water level", "Temp", "Year", "Month"]].to_numpy()

borr_model.fit(x, y.reshape(-1, 1))
print(borr_model.predict([[h, t, yr, m]]))
