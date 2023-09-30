from dash.html import Div
from dash.dcc import Graph, Dropdown

# id_venda
# entregue
# nome_produto
# quantidade
# preco_produto
# custo_produto

grafico_1 = Div(
    className = 'div-grafico',
    children = [
        Div(
            className = 'filtros',
            children = [
                Div(
                    className = 'filtro',
                    children = [
                        Dropdown(
                            id = 'dropdown_name_grafico_1',
                            options = [
                               { 'label': 'Produto', 'value': 'nome_produto' },
                               { 'label': 'Preço', 'value': 'preco_produto' },
                               { 'label': 'Custo', 'value': 'custo_produto' }
                            ],
                            value = 'nome_produto',
                            searchable = False,
                            clearable = False
                        ),
                    ]
                ),
                Div(
                    className = 'filtro',
                    children = [
                        Dropdown(
                            id = 'dropdown_value_grafico_1',
                            options = [
                               { 'label': 'Entregue', 'value': 'entregue' },
                               { 'label': 'Quantidade', 'value': 'quantidade' },
                            ],
                            value = 'entregue',
                            searchable = False,
                            clearable = False
                        ),
                    ]
                ),
            ]
        ),
        Div(
            className = 'grafico',
            children = [
                Graph(
                    id = 'grafico_1'
                )
            ]
        ),
    ]
)