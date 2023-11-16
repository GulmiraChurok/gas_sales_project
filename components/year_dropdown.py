from dash import html, dcc, Output, Input

def render(app, data):
    all_years = data['year'].unique() #to have an array of allavailable years

    @app.callback(
        Output("year-dropdown", "value"),
        Input("select-year-button", "n_clicks")
    )

    def select_all_years(n):  #n is number of clicks
        return all_years
    dropdown = html.Div(
        [
            html.H6("Year"),
            dcc.Dropdown(
                options = [{"label":year, "value":year} for year in all_years],
                multi=True,
                id = "year-dropdown"
            ),
            html.Button(
                ["Select All"],
                n_clicks=0,
                id="select-year-button"
            )
        ]
    )
    return dropdown