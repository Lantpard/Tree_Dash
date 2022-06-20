from dash import html
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/")


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Especies Arboreas de Ibague")])
            ]),

    dbc.Row([
        dbc.Col([
        html.Img(src='/assets/info.png', height="100px", width="100px"),
        html.H3("Acerca de")],class_name="card"),

        dbc.Col([
        html.Img(src='/assets/app.png', height="100px", width="100px"),
        html.H3("Monitoreo")],class_name="card"),

        dbc.Col([
        html.Img(src='/assets/arbol2.png', height="100px", width="100px"),
        html.H3("Arboles en Ibague")],class_name="arbol"),

        dbc.Col([
        html.Img(src='/assets/equipo.png', height="100px", width="100px"),
        html.H3("Equipo")],class_name="card"),

        dbc.Col([
        html.Img(src='/assets/mail.png', height="100px", width="100px"),
        html.H3("Contactanos")],class_name="card")

        ])
])