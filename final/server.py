from dash import Dash
from dash.html import Div
from components.header import header
from components.filtros import filtros
from components.body import body
from components.callbacks import registra_callback_grafico_1

app = Dash(__name__)

registra_callback_grafico_1(app)

app.layout = Div(
    children = [
        header,
        filtros,
        body
    ]
)

app.run_server(debug=True, port=8080)