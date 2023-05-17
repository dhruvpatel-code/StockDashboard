import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

def get_layout():
    return html.Div([
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
            dbc.Row([
                dbc.Col(html.Div(id='error-message'), className='mb-2')
            ]),
        ])
    ])
