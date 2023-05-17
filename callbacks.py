from dash.dependencies import Input, Output
from server import app, cache
from utils import get_data
import plotly.graph_objects as go

@app.callback(
    [Output(component_id='line-chart', component_property='figure'),
     Output(component_id='candlestick-chart', component_property='figure'),
     Output('error-message', 'children')],
    [Input(component_id='my-dropdown', component_property='value'), 
     Input(component_id='my-date-picker', component_property='start_date'),
     Input(component_id='my-date-picker', component_property='end_date'),
     Input(component_id='chart-type-dropdown', component_property='value')]
)
    
def update_graph(selected_dropdown, start_date, end_date, chart_type):

    try:
        if not selected_dropdown:
            raise ValueError("Please enter a valid stock ticker.")

        # Split the start_date and end_date to remove the time component
        start_date = start_date.split('T')[0]
        end_date = end_date.split('T')[0]

        # Fetch the stock data using the selected parameters
        df = get_data(cache, selected_dropdown, start_date, end_date)  # using cache here
        if df is None:
            raise ValueError(f"No data available for {selected_dropdown} between {start_date} and {end_date}.")
        
        # Determine the appropriate figure function based on the chart_type selection
        if chart_type == 'line':
            fig_func = go.Scatter
        elif chart_type == 'bar':
            fig_func = go.Bar
        elif chart_type == 'area':
            fig_func = go.Scatter
            fill = 'tozeroy'
        else:
            fig_func = go.Scatter
        
        # Create the traces for the line chart
        trace1 = go.Scatter(x=df.index, y=df["Close"], mode='lines', opacity=0.7, name=f'Close {selected_dropdown}', textposition='bottom center')
        trace2 = go.Scatter(x=df.index, y=df["Volume"], mode='lines', opacity=0.6, name=f'Volume {selected_dropdown}', textposition='bottom center', 
                        line=dict(color='blue'))  # Set the color for the volume line
        trace3 = go.Scatter(x=df.index, y=df["SMA"], mode='lines', opacity=0.6, name=f'SMA {selected_dropdown}', textposition='bottom center')
        trace4 = go.Scatter(x=df.index, y=df["RSI"], mode='lines', opacity=0.6, name=f'RSI {selected_dropdown}', yaxis='y2',
                        line=dict(color='red'))  # Set the color for the RSI line

        data = [trace1, trace2, trace3, trace4]

        # Create the layout for the line chart
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
        # Create the traces for the candlestick chart with RSI
        candlestick = go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'])
        rsi_trace = go.Scatter(x=df.index,
                                y=df["RSI"],
                                mode='lines',
                                opacity=0.6,
                                name=f'RSI {selected_dropdown}',
                                yaxis='y2',
                                line=dict(color='red'))

        candlestick_data = [candlestick, rsi_trace]

        # Create the layout for the candlestick chart with RSI
        candlestick_layout = go.Layout(title=f"Candlestick Chart with RSI for {selected_dropdown}",
                                       xaxis={"title":"Date",
                                                    'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 'step': 'month', 'stepmode': 'backward'},
                                                                                        {'count': 6, 'label': '6M', 'step': 'month', 'stepmode': 'backward'},
                                                                                        {'step': 'all'}])},
                                                    'rangeslider': {'visible': True}, 'type': 'date'},
                                        yaxis2={"title": "RSI", "overlaying": "y", "side": "right"})

        candlestick_figure = go.Figure(data=candlestick_data, layout=candlestick_layout)

        return line_chart_figure, candlestick_figure, ""
    except Exception as e:
        return go.Figure(), go.Figure(), f"Error: {str(e)}"

  


