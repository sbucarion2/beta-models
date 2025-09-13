import yfinance as yf

from beta_calculations import get_beta_covariance_model



aapl = yf.Ticker("AAPL")
aapl_historical = aapl.history(start="2023-01-01", end="2025-01-01", interval="1d")

spy = yf.Ticker("SPY")
spy_historical = spy.history(start="2023-01-01", end="2025-01-01", interval="1d")