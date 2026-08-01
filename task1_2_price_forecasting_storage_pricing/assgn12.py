import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import math

df = pd.read_csv("./JPMorgan/Nat_Gas.csv")
df["Dates"] = pd.to_datetime(df["Dates"], format="%m/%d/%y")
first_date = df.iloc[0, 0]
df["t"] = (df["Dates"] - first_date).dt.days
df["sint"] = np.sin(2 * np.pi * df["t"] / 365)
df["cost"] = np.cos(2 * np.pi * df["t"] / 365)
X = df.copy()
X = X.drop(columns=["Prices", "Dates"])
y = df["Prices"]
reg = LinearRegression().fit(X,y)
yhat = reg.predict(X)

def predictD(dateG):
    dateG = pd.to_datetime(dateG)
    t = (dateG - first_date).days
    sin_t = np.sin(2 * np.pi * t / 365)
    cos_t = np.cos(2 * np.pi * t / 365)
    price = reg.predict([[t, sin_t, cos_t]])
    return price[0]


def storage_contract(inj_dates, with_dates, inj_rate, with_rate, amt_values, stor_cap, stor_cost):
    if not (len(inj_dates) == len(with_dates) == len(amt_values)):
        return "INVALID"
    
    n = len(inj_dates)
    profit = 0
    current_stor = 0

    for i in range(n):
        inj_date = pd.to_datetime(inj_dates[i])
        with_date = pd.to_datetime(with_dates[i])
        amt = amt_values[i]
        if (inj_date > with_date): return "INVALID"
        avail_days = (with_date-inj_date).days
        if ((amt > inj_rate * avail_days) or (amt > with_rate * avail_days) ): return "INVALID"


    events = []
    for i in range(n):
        events.append((pd.to_datetime(inj_dates[i]), 0, amt_values[i]))
        events.append((pd.to_datetime(with_dates[i]), 1, -amt_values[i]))
    events.sort()

    for date, randomVal, amt in events:
        current_stor += amt
        if (current_stor > stor_cap or current_stor < 0): return "INVALID"

    for i in range(n):
        inj_date = pd.to_datetime(inj_dates[i])
        with_date = pd.to_datetime(with_dates[i])
        amt = amt_values[i]
        start_val = predictD(inj_date)
        exit_val = predictD(with_date)
        amt_days = (with_date-inj_date).days
        storage_cost = amt_days/30 * stor_cost
        profit += (exit_val - start_val)*amt - storage_cost

    return profit


profit = storage_contract(
    inj_dates=["2024-05-01"],
    with_dates=["2024-12-01"],
    inj_rate=500,
    with_rate=500,
    amt_values=[400],
    stor_cap=1000,
    stor_cost=100
)

print(profit)
