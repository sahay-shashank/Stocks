# Yahoo Finance is used to gather real-time and historical stocks data from Yahoo
import yahooquery as yf
# matplotlib is used to plot the data in a graph
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import json
from flask import Flask, request , render_template, redirect
app = Flask(__name__)

@app.route('/')
def rendering():
    return render_template('plot.html')
    
@app.route('/plotgraph',methods=['POST']) # type: ignore
def plot():
    result = request.get_json()
    print(result)
    # takes ticker to get stock data
    company = yf.Ticker(result['ticker'],country="India")
    # gets the history for the ticker
    stock_history = company.history(result['period'], result['interval'])
    if(stock_history.empty):
        print("Not available")
        return {'result': 0}
    values_of_option = stock_history[result['option'].lower()]
    fig = go.Figure(data=[go.Scatter(x=values_of_option.index.get_level_values("date"), y=values_of_option.values)], layout=go.Layout(
        xaxis=go.layout.XAxis(showline=True, showspikes=True, spikedash="solid",
                            spikemode="toaxis+across", spikethickness=1, spikecolor="red")
    ))
    # plots in a graph
    plot_json = fig.to_json()
    return {'profile': json.dumps(company.asset_profile),'result_plot':plot_json}
    # return plot_json

if __name__=='__main__':
    app.run(debug=True)