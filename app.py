import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from flask_caching import Cache
import ta

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Stock Dashboard", className='text-center text-primary, mb-4'), className='mb-2 mt-2')
        ]),
        dbc.Row([
            dbc.Col(dcc.Input(id='my-dropdown', type='text', value='AAPL', debounce=True, className='mb-3'))
    ]),

        dbc.Row([
            dbc.Col(dcc.DatePickerRange(id='my-date-picker', min_date_allowed=pd.to_datetime('2015-01-01'),
                                        max_date_allowed=pd.to_datetime('2025-12-31'), start_date=pd.to_datetime('2020-01-01'),
                                        end_date=pd.to_datetime('2022-12-31'), className='mb-3'))
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='line-chart'), className='mb-2'),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='candlestick-chart'), className='mb-2'),
        ]),
    ])
])

@app.callback(
    [Output(component_id='line-chart', component_property='figure'),
     Output(component_id='candlestick-chart', component_property='figure')],
    [Input(component_id='my-dropdown', component_property='value'), 
     Input(component_id='my-date-picker', component_property='start_date'),
     Input(component_id='my-date-picker', component_property='end_date')]
)
def update_graph(selected_dropdown, start_date, end_date):
    start_date = start_date.split('T')[0]
    end_date = end_date.split('T')[0]
    df = get_data(selected_dropdown, start_date, end_date)
    if df is None:
        return go.Figure(), go.Figure()

    trace1 = go.Scatter(x=df.index, y=df["Close"], mode='lines', opacity=0.7, name=f'Close {selected_dropdown}', textposition='bottom center')
    
    trace2 = go.Scatter(x=df.index, y=df["Volume"], mode='lines', opacity=0.6, name=f'Volume {selected_dropdown}', textposition='bottom center', 
                        line=dict(color='blue'))  # Set the color for the volume line
    
    trace3 = go.Scatter(x=df.index, y=df["SMA"], mode='lines', opacity=0.6, name=f'SMA {selected_dropdown}', textposition='bottom center')
    
    trace4 = go.Scatter(x=df.index, y=df["RSI"], mode='lines', opacity=0.6, name=f'RSI {selected_dropdown}', yaxis='y2',
                        line=dict(color='red'))  # Set the color for the RSI line

    data = [trace1, trace2, trace3, trace4]
    

    line_chart_figure = {'data': data,
                         'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
                                             height=600,
                                             title=f"Closing Prices, Volume, SMA and RSI for {selected_dropdown} Over Time",
                                             xaxis={"title":"Date",
                                                    'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 'step': 'month', 'stepmode': 'backward'},
                                                                                       {'count': 6, 'label': '6M', 'step': 'month', 'stepmode': 'backward'},
                                                                                       {'step': 'all'}])},
                                                    'rangeslider': {'visible': True}, 'type': 'date'},
                                             yaxis={"title":"Price / Volume"},
                                             yaxis2={"title":"RSI", "overlaying":"y", "side":"right"}  # Add a secondary y-axis for RSI
                                            )
                         }
    
    candlestick = go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'])

    candlestick_data = [candlestick]

    candlestick_layout = go.Layout(title=f"Candlestick Chart for {selected_dropdown}")

    candlestick_figure = go.Figure(data=candlestick_data, layout=candlestick_layout)

    return line_chart_figure, candlestick_figure

@cache.memoize()
def get_data(selected_dropdown, start_date, end_date):
    try:
        df = yf.download(selected_dropdown, start=start_date, end=end_date)
        df.sort_values('Date', inplace=True)
        
        # Add SMA and RSI to the dataframe
        df['SMA'] = ta.trend.sma_indicator(df['Close'], window=14)
        df['RSI'] = ta.momentum.rsi(df['Close'], window=14)

        return df
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


if __name__ == '__main__':
    app.run_server(debug=True)




