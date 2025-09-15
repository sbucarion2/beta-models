import yfinance as yf

from beta_calculations import get_beta_covariance_model, get_pct_change



aapl = yf.Ticker("AAPL")
aapl_historical = aapl.history(start="2023-01-01", end="2025-01-01", interval="1d")

spy = yf.Ticker("SPY")
spy_historical = spy.history(start="2023-01-01", end="2025-01-01", interval="1d")

beta = get_beta_covariance_model(
    list(aapl_historical["Close"]),
    list(spy_historical["Close"])
)

trading_dates = spy_historical.index

aapl_pct = get_pct_change(list(aapl_historical["Close"]))
spy_pct = get_pct_change(list(spy_historical["Close"]))

positive_change = []
negative_change = []
mistmatched = []
for aa, sp in zip(aapl_pct, spy_pct):

    if aa > 0 and sp > 0:

        positive_change.append((aa, sp))

        continue

    if aa < 0 and sp < 0:

        negative_change.append((aa, sp))

        continue

    if aa != 0 and sp != 0:

        mistmatched.append((aa,sp))

long_beta = get_beta_covariance_model(
    [aa for aa,sp in positive_change],
    [sp for aa,sp in positive_change]
)
print(long_beta)

short_beta = get_beta_covariance_model(
    [aa for aa,sp in negative_change],
    [sp for aa,sp in negative_change]
)
print(short_beta)


print(mistmatched)
mismatched_beta = get_beta_covariance_model(
    [aa for aa,sp in mistmatched],
    [sp for aa,sp in mistmatched]
)
print(mismatched_beta)


test_beta = get_beta_covariance_model(
    [aa for aa,sp in positive_change]+[aa for aa,sp in negative_change]+[aa for aa,sp in mistmatched],
    [sp for aa,sp in positive_change]+[sp for aa,sp in negative_change]+[sp for aa,sp in mistmatched]
)
print("TB", test_beta)

real_beta = get_beta_covariance_model(
    list(aapl_historical["Close"]),
    list(spy_historical["Close"])
)
print("RB", real_beta)

# print(positive_change)
# print(len(positive_change), len(trading_dates))
# print(len(negative_change), len(trading_dates))
# print(len(positive_change)+len(negative_change), len(trading_dates))
# Get pct change for array then map the pct_changes from x and y where they are both in same direction

# for date in trading_dates:

#     print(spy_historical.loc[date]["Open"], aapl_historical.loc[date]["Open"])
#     break

# print(beta)

# print(aapl_historical, spy_historical)
