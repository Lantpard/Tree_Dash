import dash
import dash_labs as dl
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.CYBORG]
)

navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("Home", href="/")),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    dbc.NavItem(dbc.NavLink("Nosotros", href="/nosotros")),
    ],
    brand="Team 123",
    color="dark",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port=8050, debug=True)