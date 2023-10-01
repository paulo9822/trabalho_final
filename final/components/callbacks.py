from dash import Output, Input
import pandas as pd
import plotly.express as px
from data.Data import Data

# Dicionário que mapeia 'nome_produto' para cores
cor_por_produto = {
    'Mouse': 'blue',
    'Teclado': 'green',
    'Monitor': 'red',
    'Desktop': 'purple',
    'Processador': 'orange'
}

def registra_callback_grafico_1(app):
    @app.callback(
        Output('grafico_1', 'figure'),
        Input('global_intervalo_id_venda', 'value'),
        Input('dropdown_name_grafico_1', 'value'),
        Input('dropdown_value_grafico_1', 'value'),
        Input('dropdown_funcao_grafico_1', 'value')
    )
    def render(global_intervalo_id_venda, dropdown_name_grafico_1, dropdown_value_grafico_1, dropdown_funcao_grafico_1):
        dados = Data.vendas.query(f'{global_intervalo_id_venda[0]} <= entregue <= {global_intervalo_id_venda[1]}')
        
        if dropdown_value_grafico_1 == 1:  # Verifica se o valor é 1 (Entregue)
            dados_filtrados = dados[dados['entregue'] == 1]
        elif dropdown_value_grafico_1 == 0:  # Verifica se o valor é 0 (Não Entregue)
            dados_filtrados = dados[dados['entregue'] == 0]
        else:
            dados_filtrados = dados  # Use todos os dados se o valor não for 0 ou 1
            
        if dropdown_funcao_grafico_1 == 'Soma':
            dados_filtrados = dados_filtrados.groupby(dropdown_name_grafico_1).sum().reset_index()
        elif dropdown_funcao_grafico_1 == 'Média':
            dados_filtrados = dados_filtrados.groupby(dropdown_name_grafico_1).mean().reset_index()

        fig = px.pie(
            dados_filtrados,
            names=dropdown_name_grafico_1,
            values=dropdown_value_grafico_1,
            color=dropdown_name_grafico_1,  # Define a cor com base na coluna 'nome_produto'
            color_discrete_map=cor_por_produto  # Mapeia 'nome_produto' para cores personalizadas
        )
        return fig
