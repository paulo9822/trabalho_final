from dash import Output, Input
import pandas as pd
import plotly.express as px
from data.Data import Data

# id_venda
# entregue
# nome_produto
# quantidade
# preco_produto
# custo_produto

def registra_callback_grafico_1(app):
    @app.callback(
        Output('grafico_1', 'figure'),
        Input('global_intervalo_id_venda', 'value'),
        Input('dropdown_name_grafico_1', 'value'),
        Input('dropdown_value_grafico_1', 'value')
    )
    def render(global_intervalo_id_venda, dropdown_name_grafico_1, dropdown_value_grafico_1):
        dados = Data.vendas.query(f'{global_intervalo_id_venda[0]} <= id_venda <= {global_intervalo_id_venda[1]}')
        if dropdown_value_grafico_1 == 0:
            dados_filtrados = dados[dados['entregue'] == 0]
        else:
            dados_filtrados = dados[dados['entregue'] == 1]
        fig = px.pie(
            dados_filtrados,
            names=dropdown_name_grafico_1,
            values=dropdown_value_grafico_1
        )
        return fig
