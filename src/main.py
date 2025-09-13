import numpy as np
import yfinance as yf
from typing import List
import statsmodels.api as sm

def get_pct_change(array: List[float]):

    pct_change = []
    for i in range(1, len(array)):

        pct_change.append((array[i] - array[i-1]) / array[i-1])

    return pct_change



ticker = yf.Ticker("RSG")

# aapl_historical = ticker.history(start="2025-08-02", end="2025-08-07", interval="1m")

# aapl_historical = ticker.history(start="2025-08-02", end="2025-08-29", interval="1d")

aapl = yf.Ticker("AAPL")
aapl_historical = aapl.history(start="2023-01-01", end="2025-01-01", interval="1d")



spy = yf.Ticker("SPY")
spy_historical = spy.history(start="2023-01-01", end="2025-01-01", interval="1d")

# print("Prices:", aapl_historical)

# beta*x = y
# X=b
# A=y
# beta*b = A 
# or beta*b-A=0

# beta = covar(x,y) / var(x)
# beta = covar(B,A) / var(B)

# x=predictor
# y=responder


aapl_pct_change = get_pct_change(list(aapl_historical['Close']))
spy_pct_change = get_pct_change(list(spy_historical['Close']))

covariance = np.cov(
        spy_pct_change, 
        aapl_pct_change
    )[0][1]
variance = np.var(spy_pct_change)

print(covariance / variance)

covariance = np.cov(
        aapl_pct_change, 
        spy_pct_change
    )[0][1]
variance = np.var(spy_pct_change)

print(covariance / variance)

# result = np.cov(spy_historical["Close"],aapl_historical["Close"])
# x_y_cov = result[0][1]

# print(np.var(spy_historical["Close"]))

# print(x_y_cov/np.var(spy_historical["Close"]))


def get_hedge_ratio(a_data, b_data):
    """Linear Regression, a, first ticker in pair, is x
        b is the second ticker, y. X is IV and y is DV. 
        The ratio is used the create the spread for the ticker"""
    a_constant = sm.add_constant(a_data)
    
    #Run linear regression on the pairs data for ratio
    results = sm.OLS(b_data,a_constant).fit()
    
    ratio = results.params[1] 

    return float(ratio)

print("b: ", get_hedge_ratio(spy_pct_change, aapl_pct_change))