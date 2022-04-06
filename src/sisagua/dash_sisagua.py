#!/usr/bin/env python
# coding: utf-8


import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from src.sisagua.git_api import *
from src.sisagua.vig import *

# Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Divs
app.layout = html.Div(
    children=[
        # Header
        html.Div([
            html.H1(children='Siságua', style={'text-align': 'center'}),
            html.Div("""
            Painel construído com dados do Siságua, obtidos no Portal de Dados Abertos.
            """),
            html.Br(),
            html.Div('Michel Metran da Silva'),
            html.A('Repositório', href='https://github.com/open-geodata/br_sisagua'),
            html.Br(),
            html.Br(),
        ]),

        # Cadastro
        html.Div(
            [
                html.Div('Escolha o município: '),
                dcc.Dropdown(
                    id='dd-municipio',
                    options=list_cities,
                    # value='Fertility rate, total (births per woman)',
                ),
            ],
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'}
        ),

        #
        html.Div(
            [
                html.Div('Escolha a Forma De Abastecimento: '),
                dcc.Dropdown(
                    id='dd-forma-abastecimento',
                    options=df['Nome Da Forma De Abastecimento'].unique(),
                    # value='Fertility rate, total (births per woman)',
                ),
            ],
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'}
        ),

        # Vigilância
        html.Div(
            dcc.Graph(id='graphic-cloro'),
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'},
        ),
    ]
)


@app.callback(
    Output('graphic-cloro', 'figure'),
    Input('dd-forma-abastecimento', 'value'),
)
def update_graph(forma_abastecimento):
    # Create Figure
    fig = go.Figure()

    # Add trace
    fig.add_trace(
        go.Scatter(
            x=df['Data Da Coleta'],
            y=df[df['Nome Da Forma De Abastecimento'] == forma_abastecimento]['Resultado'],
            name='conclusao',
            mode='markers',
            marker={'color': 'red'},
            opacity=0.8,
        )
    )

    # Update
    fig.update_layout(
        title='Cloro Residual na "{}"'.format(forma_abastecimento),
        xaxis_tickformat='%d %b<br>%Y',
        margin={
            'l': 40,
            'b': 40,
            # 't': 40,
            'r': 0
        },
        # dragmode='pan',
        hovermode='x',

    )
    return fig


if __name__ == '__main__':
    app.run_server(
        # debug=True
    )

# # Paths
# output_path_dados = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         '..', '..',
#         'data',
#         'output',
#     )
# )

# os.path.join(output_path_dados, str(id_ibge), 'dados brutos', 'vigilancia', 'vigilancia_parametros_basicos.xlsx'),
