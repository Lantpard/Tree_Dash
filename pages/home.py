from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/")


layout = dbc.Row([
    dbc.Col([
    html.Div("This is the home page")]),
    dbc.Col([
    html.Img(src='/assets/404.png')])])