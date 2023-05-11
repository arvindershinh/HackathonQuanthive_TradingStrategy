import talib as ta
from blueshift.library.technicals.indicators import sma
from blueshift.api import symbol, schedule_function, order_target_percent
from blueshift.api import date_rules, time_rules

def initialize(context):
    context.freq = 1
    context.asset = symbol('HAL')
    schedule_function(rebalance, date_rules.every_day(),time_rules.every_nth_hour(context.freq))

def rebalance(context, data):
    price = data.history(context.asset, 'close', 255, '1d')
    signal = signal_func(context.asset, price)
    order_target_percent(context.asset, signal)

def signal_func(asset, price):
    rsi = ta.RSI(price, 57)[-1]
    fast_ma = sma(price, 50)
    slow_ma = sma(price, 200)

    if (rsi < 30) or (fast_ma > slow_ma) :
        return 1  # buy signal
    elif rsi > 70:
        return -1 # sell signal
    else:
        return 0  # neutral signal

# lag 30 --> 0.07	0 %
# lag 50 --> 0.98	1 %
# lag 53 --> 0.98	1 %
# lag 54 --> 1.4	2 %
# lag 55 --> 1.4	2 %
# lag 56 --> 1.4	2 %
# lag 57 --> 1.4	2 %
# lag 58 --> 1.4	2 %
# lag 58 --> 1.4	2 %
# lag 60 --> 0	    0 %
# lag 70 --> 0	    0 %

# lag 100 --> 0	    0 %
# lag 200 --> 0	    0 %

# lag XX -->