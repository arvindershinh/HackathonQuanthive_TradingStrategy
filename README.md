# HackathonQuanthive_TradingStrategy
 Build a trading strategy, that satisfies the given benchmark metrics.

Recommended backtest setting:
* Dataset : NSE
* Starting Capital: 10000
* Start Date: January 1, 2022
* End Date: December 31, 2022
* Shorting is allowed: Yes

Participants have two options:

* Build a trading strategy of your choice either in No-code or Python coding builder. That satisfies the given benchmark metrics below.
* Build a Relative Strength Index (RSI) trading strategy using either No-code or Python coding builder. Here is an article on RSI

Strategy Setting:
* Asset: HAL
* Data frequency: 1 minute
* RSI lookback : 15*
* Schedule Frequency: every 1 hour

Trade Signals:
* Long/Buy 100% of the account in the asset when RSI goes below 30.
* Short/Sell 100% of the account in the asset when RSI goes above 70.
