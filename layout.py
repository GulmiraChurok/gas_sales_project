from dash import html
import dash_bootstrap_components as dbc
from components import year_dropdown, pie_chart, month_dropdown, category_dropdown

def create_layout(app, data):
    return dbc.Container(
        [
           dbc.Row(dbc.Col(html.H1("Gas Sales Project"))),
           dbc.Row(
                   [
                       dbc.Col([
                            year_dropdown.render(app,data), 
                            month_dropdown.render(app,data),
                            category_dropdown.render(app,data)
                       ],lg=4),
                       dbc.Col(pie_chart.render(app,data),lg=8)
                   ]
                   )
        ]
    )