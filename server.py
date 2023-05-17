import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

# This is needed for running the app with gunicorn for deployment
server = app.server
