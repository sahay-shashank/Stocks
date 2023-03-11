# Yahoo Finance is used to gather real-time and historical stocks data from Yahoo
import yahooquery as yf
# matplotlib is used to plot the data in a graph
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# takes ticker to get stock data
t = yf.Ticker('SBIN.NS')
print(t)
# gets the history for the ticker
thist = t.history("5y", "1d")
items = thist["close"]
fig = go.Figure(data=[go.Scatter(x=items.index.get_level_values("date"), y=items.values)], layout=go.Layout(
    xaxis=go.layout.XAxis(showline=True, showspikes=True, spikedash="solid",
                          spikemode="toaxis+across", spikethickness=1, spikecolor="red")
))
# plots in a graph
# fig.write_html("plot.html")
fig.show()
