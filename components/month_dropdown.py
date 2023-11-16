from dash import html, dcc, Output, Input

def render(app,data):
    all_months = data['month'].unique()
    options = [{"label":month, "value":month} for month in all_months]
    @app.callback(
        Output("month-dropdown","value"),
        [
            Input("year-dropdown","value"),
            Input("month_button","n_clicks")
        ]
    )
    def select_all_months(years,n):
        filtered_data = data.query("year in @years")
        return sorted(filtered_data["month"].unique())
    return html.Div(
        [
            html.H6("Month"),
            dcc.Dropdown(
                options=options,
                multi=True, 
                id = "month-dropdown"
            ),
            html.Button(
                ["Select All"],
                id="month_button",
                n_clicks=0
            )
        ]
        
    )