import dash 
import dash_bootstrap_components as dbc
from flask_caching import Cache

app = dash.Dash(__name__,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.MATERIA])
server = app.server
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})