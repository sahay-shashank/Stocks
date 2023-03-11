# Yahoo Finance is used to gather real-time and historical stocks data from Yahoo
import yahooquery as yf
# matplotlib is used to plot the data in a graph
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import json
import csv

from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__, static_url_path="/static")


@app.route('/')
def rendering():
    return render_template('index.html')


@app.route('/plotgraph', methods=['POST'])
def plot():
    result = request.get_json()
    print(result)
    # takes ticker to get stock data
    company = yf.Ticker(result['ticker'], country="India")
    # gets the history for the ticker
    stock_history = company.history(result['period'], result['interval'])
    if (stock_history.empty):
        print("Not available")
        return {'result': 0}
    values_of_option = stock_history[result['option'].lower()]
    fig = go.Figure(data=[go.Scatter(x=values_of_option.index.get_level_values("date"), y=values_of_option.values)], layout=go.Layout(
        xaxis=go.layout.XAxis(showline=True, showspikes=True, spikedash="solid",
                              spikemode="toaxis+across", spikethickness=1, spikecolor="red"),
        yaxis=go.layout.YAxis(
            title=company.summary_detail[result['ticker']]['currency'])  # type: ignore
    ))
    # plots in a graph
    plot_json = fig.to_json()
    print()
    return {'profile': json.dumps(company.summary_profile), 'result_plot': plot_json}
    # return plot_json

@app.route('/getticker',methods = ["POST"])
def getticker():
    company = request.get_json()["company"].lower()
    with open('constituents.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {row['Name'].lower(): row['Symbol'] for row in reader}
    print(data.get(company))
    ticker = data.get(company)
    return json.dumps({'ticker':ticker})

@app.route('/graph')
def graph():
    ticker = request.args.get("ticker")
    name = request.args.get('name')
    return render_template('graph.html',ticker_graph = ticker, name = name)

if __name__ == '__main__':
    app.run(debug=True)
