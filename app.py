# Yahoo Finance is used to gather real-time and historical stocks data from Yahoo
import yfinance as yf
# matplotlib is used to plot the data in a graph
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import json
from flask import Flask, request , render_template, redirect
app = Flask(__name__)

@app.route('/')
def rendering():
    return render_template('form.html')
    
@app.route('/plot',methods=['POST'])
def plot():
    data = request.get_json()
    result = json.loads(data)
    print(result)
    # takes ticker to get stock data
    t = yf.Ticker(result['ticker'])
    # gets the history for the ticker
    thist = t.history(result['period'], result['interval'])
    items = thist[result['option']]
    fig = go.Figure(data=[go.Scatter(x=items.index, y=items.values)], layout=go.Layout(
        xaxis=go.layout.XAxis(showline=True, showspikes=True, spikedash="solid",
                            spikemode="toaxis+across", spikethickness=1, spikecolor="red")
    ))
    # plots in a graph
    fig.write_html("plot_frame.html")
    # plot_json = fig.to_json()
    # print(plot_json)
    print('Done')
    fig.show()
    return render_template('plot.html')
if __name__=='__main__':
    app.run(debug=True)