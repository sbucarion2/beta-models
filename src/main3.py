import yfinance as yf

from beta_calculations import get_beta_covariance_model, get_pct_change


aapl = yf.Ticker("AAPL")
aapl_historical = aapl.history(start="2024-01-01", end="2025-01-01", interval="1d")

spy = yf.Ticker("SPY")
spy_historical = spy.history(start="2024-01-01", end="2025-01-01", interval="1d")

beta = get_beta_covariance_model(
    list(aapl_historical["Close"]),
    list(spy_historical["Close"])
)

trading_dates = spy_historical.index

aapl_pct_change = get_pct_change(list(aapl_historical["Close"]))
spy_pct_change = get_pct_change(list(spy_historical["Close"]))

positive_market_change = []
negative_market_change = []
for aapl_pct,spy_pct in zip(aapl_pct_change, spy_pct_change):

    if spy_pct > 0 and aapl_pct != 0:

        positive_market_change.append((aapl_pct,spy_pct))

    if spy_pct < 0 and aapl_pct != 0:

        negative_market_change.append((aapl_pct,spy_pct))


positive_beta = get_beta_covariance_model(
    [security_point for security_point, market_point in positive_market_change],
    [market_point for security_point, market_point in positive_market_change],
    pct_change_passed=True
)

negative_beta = get_beta_covariance_model(
    [security_point for security_point, market_point in negative_market_change],
    [market_point for security_point, market_point in negative_market_change],
    pct_change_passed=True
)

print("FULL BETA: ", beta)
print("POSITIVE BETA: ", positive_beta)
print("NEGTIVE BETA: ", negative_beta)
