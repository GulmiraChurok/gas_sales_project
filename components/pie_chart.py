import plotly.express as px
from dash import dcc, html, Input, Output

def render(app, data):
    @app.callback(
        Output("pie_chart", "children"),
        [
            Input("year-dropdown", "value"),
            Input("month-dropdown","value"),
            Input("category-dropdown","value"),
        ]
)
    def update_pie_chart(years, months, categories):
        filtered_data = data.query("year in @years and month in @months and category in @categories")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected", id="pie_chart")
        fig = px.pie(filtered_data, 
                    values="amount",
                    names="category",
                    hole = 0.4
                    )
        return html.Div(dcc.Graph(figure = fig), id="pie_chart")
    return html.Div(id="pie_chart")