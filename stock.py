# Yahoo Finance is used to gather real-time and historical stocks data from Yahoo
import yfinance as yf
# matplotlib is used to plot the data in a graph
import matplotlib.pyplot as plt


# takes ticker to get stock data
t = yf.Ticker('SBIN.NS')
print(t)
# gets the history for the ticker
thist = t.history("1d", "1m")
print(thist)
# plots in a graph
thist["Close"].plot()
plt.show()
