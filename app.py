import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Stock Dashboard", className='text-center text-primary, mb-4'), className='mb-2 mt-2')
        ]),
        dbc.Row([
            dbc.Col(dcc.Dropdown(id='my-dropdown',
                                 options=[
                                     {'label': 'Apple', 'value': 'AAPL'},
                                     {'label': 'Amazon', 'value': 'AMZN'},
                                     {'label': 'Microsoft', 'value': 'MSFT'}
                                 ],
                                 multi=True,
                                 value=['AAPL'],
                                 style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "60%"}), className='mb-3')
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='line-chart'), className='mb-2'),
        ]),
    ])
])


@app.callback(
    Output(component_id='line-chart', component_property='figure'),
    [Input(component_id='my-dropdown', component_property='value')]
)
def update_graph(selected_dropdown):
    dropdown = {"AAPL": "Apple","AMZN": "Amazon","MSFT": "Microsoft",}
    trace1 = []
    trace2 = []
    for stock in selected_dropdown:
        df = yf.download(stock, start="2018-01-01", end="2022-12-31")
        df.sort_values('Date', inplace=True)
        trace1.append(go.Scatter(x=df.index, y=df["Close"], mode='lines', opacity=0.7, name=f'Close {dropdown[stock]}',textposition='bottom center'))
        trace2.append(go.Scatter(x=df.index, y=df["Volume"], mode='lines', opacity=0.6, name=f'Volume {dropdown[stock]}',textposition='bottom center'))
    traces = [trace1, trace2]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                                  height=600,
                                  title=f"Closing Prices for {', '.join(str(dropdown[i]) for i in selected_dropdown)} Over Time",
                                  xaxis={"title":"Date",
                                         'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 'step': 'month', 'stepmode': 'backward'},
                                                                            {'count': 6, 'label': '6M', 'step': 'month', 'stepmode': 'backward'},
                                                                            {'step': 'all'}])},
                                         'rangeslider': {'visible': True}, 'type': 'date'},
                                  yaxis={"title":"Price (USD)"})}
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
