import flask
from sklearn.ensemble import RandomForestRegressor as forest
from sklearn.model_selection import train_test_split as spl
import pandas as pd
from flask import Flask, request
import numpy as np
import warnings
warnings.filterwarnings('ignore')

dp = "../processed_data/"

darw_model = forest(n_estimators = 500)
kath_model = forest(n_estimators = 500)
nhul_model = forest(n_estimators = 500)
borr_model = forest(n_estimators = 500)

darw_data = pd.read_csv(dp+"Darwin_ml_data.csv")
darw_data = darw_data[darw_data["Temp"] != -10][darw_data["Water level"] != -10]

y = darw_data[["Crocs"]].to_numpy()
x = darw_data[["Water level", "Temp", "Year", "Month"]].to_numpy()

darw_model.fit(x, y.reshape(-1, 1))

kath_data = pd.read_csv(dp+"Katherine_ml_data.csv")
kath_data = kath_data[kath_data["Temp"] != -10][kath_data["Water level"] != -10]

y = kath_data[["Crocs"]].to_numpy()
x = kath_data[["Water level", "Temp", "Year", "Month"]].to_numpy()

kath_model.fit(x, y.reshape(-1, 1))

nhul_data = pd.read_csv(dp+"Nhulunbuy_ml_data.csv")
nhul_data = nhul_data[nhul_data["Temp"] != -10]

y = nhul_data[["Crocs"]].to_numpy()
x = nhul_data[["Temp", "Year", "Month"]].to_numpy()

nhul_model.fit(x, y.reshape(-1, 1))

borr_data = pd.read_csv(dp+"Borroloola_ml_data.csv")
borr_data = borr_data[borr_data["Temp"] != -10][borr_data["Water level"] != -10]

y = borr_data[["Crocs"]].to_numpy()
x = borr_data[["Water level", "Temp", "Year", "Month"]].to_numpy()

borr_model.fit(x, y.reshape(-1, 1))

app = Flask(__name__)

@app.route("/Darwin")
def darwin():
    wl = request.args.get('wl')
    tmp = request.args.get('tmp')
    yr = request.args.get('yr')
    mo = request.args.get('mo')
    res = str(darw_model.predict([[float(wl), float(tmp), float(yr), float(mo)]])[0])
    resp = flask.Response(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/Katherine")
def kath():
    wl = request.args.get('wl')
    tmp = request.args.get('tmp')
    yr = request.args.get('yr')
    mo = request.args.get('mo')
    res = str(kath_model.predict([[float(wl), float(tmp), float(yr), float(mo)]])[0])
    resp = flask.Response(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/Nhulunbuy")
def nhul():
    tmp = request.args.get('tmp')
    yr = request.args.get('yr')
    mo = request.args.get('mo')
    res = str(nhul_model.predict([[float(tmp), float(yr), float(mo)]])[0])
    resp = flask.Response(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/Borroloola")
def borr():
    wl = request.args.get('wl')
    tmp = request.args.get('tmp')
    yr = request.args.get('yr')
    mo = request.args.get('mo')
    res = str(borr_model.predict([[float(wl), float(tmp), float(yr), float(mo)]])[0])
    resp = flask.Response(res)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp