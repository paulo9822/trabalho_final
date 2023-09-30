from dash.html import Div
from components.graficos.grafico_1 import grafico_1

body = Div(
    id = 'body',
    children = [
        grafico_1
    ]
)