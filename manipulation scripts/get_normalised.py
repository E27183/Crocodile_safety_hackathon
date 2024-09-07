import pandas as pd
import numpy as np
import os

min_year = 1999
max_year = 2023

dp = "../data/"

captures = pd.read_csv(dp+"Nt Croc Capture.csv")
borr_wl = pd.read_csv(dp+"Boroloola_water_level_history.csv")
borr_mt = pd.read_csv(dp+"Borroloola_max_temp_history.csv")
darw_wl = pd.read_csv(dp+"Darwin_water_level_history.csv")
darw_mt = pd.read_csv(dp+"Darwin_max_temp_history.csv")
kath_mt = pd.read_csv(dp+"Katherine_max_temp_history.csv")
kath_wl = pd.read_csv(dp+"Katherine_water_level_history.csv")
nhul_mt = pd.read_csv(dp+"Nhulunbuy_max_temp_history.csv")

import warnings
warnings.filterwarnings('ignore')

borr_wl["Timestamp (UTC+09:30)"] = borr_wl["Timestamp (UTC+09:30)"].apply(lambda x: x[0:10])
darw_wl["Timestamp (UTC+09:30)"] = borr_wl["Timestamp (UTC+09:30)"].apply(lambda x: x[0:10])
kath_wl["Timestamp (UTC+09:30)"] = borr_wl["Timestamp (UTC+09:30)"].apply(lambda x: x[0:10])

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#leap year -> year % 4 == 0

total_days = sum(days_per_month)*(max_year - min_year + 1) + 6

borr_data = np.zeros((total_days, 4)) #one array per day all data

index = 0

for i in range(25):
    print(i+1999)
    for j in range(12):
        leap = 1 if j == 1 and i % 4 == 1 else 0
        for k in range(days_per_month[j] + leap):
            if index >= 9131:
                np.savetxt(dp+"Nhulunbuy_ml_data.csv", borr_data, delimiter=", ")
            datestring = str(1999 + i) + '-' + str(j + 1).zfill(2) + '-' + str(k + 1).zfill(2)
            # b_wls = kath_wl[kath_wl['Timestamp (UTC+09:30)'] == datestring]["Value (m)"]
            # b_wla = b_wls.mean()
            # borr_data[index][1] = b_wla
            b_crocs = captures[captures["REGION"] == "Nhulunbuy"][captures["DATE_CAPTURED"] == datestring]
            borr_data[index][0] = b_crocs.shape[0]
            b_tmps = nhul_mt[nhul_mt["Year"] == i + 1999][nhul_mt["Month"] == j + 1][nhul_mt["Day"] == k + 1]
            borr_data[index][1] = b_tmps["Maximum temperature (Degree C)"].mean()
            borr_data[index][2] = 1999 + i
            borr_data[index][3] = j
            index+=1

np.savetxt(dp+"Nhulunbuy_ml_data.csv", borr_data, delimiter=", ")