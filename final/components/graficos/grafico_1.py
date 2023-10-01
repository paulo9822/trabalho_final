from dash.html import Div
from dash.dcc import Graph, Dropdown

grafico_1 = Div(
    className='div-grafico',
    children=[
        Div(
            className='filtros',
            children=[
                Div(
                    className='filtro',
                    children=[
                        Dropdown(
                            id='dropdown_name_grafico_1',
                            options=[
                                {'label': 'Produtos', 'value': 'nome_produto'},
                                {'label': 'Mouse', 'value': 'Mouse'},
                                {'label': 'Teclado', 'value': 'Teclado'},
                                {'label': 'Monitor', 'value': 'Monitor'},
                                {'label': 'Desktop', 'value': 'Desktop'},
                                {'label': 'Processador', 'value': 'Processador'}
                            ],
                            value='nome_produto',
                            searchable=False,
                            clearable=False
                        ),
                    ]
                ),
                Div(
                    className='filtro',
                    children=[
                        Dropdown(
                            id='dropdown_value_grafico_1',
                            options=[
                                {'label': 'Entregue', 'value': 1},
                                {'label': 'Não entregue', 'value': 0},
                                {'label': 'Preço', 'value': 'preco_produto'},
                                {'label': 'Custo', 'value': 'custo_produto'},
                                {'label': 'Quantidade vendida', 'value': 'quantidade'}
                            ],
                            value='filtro',
                            searchable=False,
                            clearable=False
                        ),
                        Dropdown(
                            id='dropdown_funcao_grafico_1',
                            options=['Soma', 'Média'],
                            value='Soma',
                            clearable=False
                        )
                    ]
                ),
            ]
        ),
        Div(
            className='grafico',
            children=[
                Graph(
                    id='grafico_1'
                )
            ]
        ),
    ]
)
