from dash.html import Div
from dash.dcc import RangeSlider

filtros = Div(
    id = 'filtros-globais',
    children = [
        RangeSlider(
            id = 'global_intervalo_id_venda',
            min = 0,
            max = 10,
            value = [0,10]
        )
    ]
)