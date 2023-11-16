from dash import html, dcc, Output, Input

def render(app,data):
    all_categories = data['category'].unique()
    options = [{"label":category, "value":category} for category in all_categories]
    @app.callback(
        Output("category-dropdown","value"),
        [
            Input("year-dropdown","value"),
            Input("month-dropdown","value"),
            Input("category_button","n_clicks")
        ]
    )
    def select_all_categories(years, months,n):
        filtered_data = data.query("year in @years and month in @months")
        return sorted(filtered_data["category"].unique())
    return html.Div(
        [
            html.H6("Category"),
            dcc.Dropdown(
                options=options,
                multi=True, 
                id = "category-dropdown"
            ),
            html.Button(
                ["Select All"],
                id="category_button",
                n_clicks=0
            )
        ]
        
    )