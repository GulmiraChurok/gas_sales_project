from dash import Dash, html             
import dash_bootstrap_components as dbc
from util import get_data
from layout import create_layout
import os


PATH = os.path.join(os.getcwd(), "gas_sale.csv")

data = get_data(PATH)
# df = pd.read_csv(PATH) 
print(data)

app = Dash(external_stylesheets=[dbc.themes.CYBORG])

app.title = "Gas sale"

app.layout = create_layout(app,data)

app.run_server(debug=True)
