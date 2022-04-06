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
            html.H1(children='Siságua', style={'text-align': 'left'}),
            html.P('Painel construído com dados do Siságua, obtidos no Portal de Dados Abertos.'),
            html.P('Elaborando visando avaliar o atendimento a Portaria MS 05/17'),
            html.Br(),
            html.P('Michel Metran da Silva'),
            html.A('Repositório', href='https://github.com/open-geodata/br_sisagua'),
            html.Hr(),
        ]),

        # Controles
        html.H2(children='Controles'),
        html.Div(
            children=[
                html.Div('Escolha o município: '),
                dcc.Dropdown(
                    id='dd-municipio',
                    options=list_cities,
                    placeholder='Selecione um município utilizando o código IBGE',
                    # value='Fertility rate, total (births per woman)',
                ),
            ],
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'}
        ),

        #
        html.Div(
            [
                html.Div('Escolha a Forma de Abastecimento: '),
                dcc.Dropdown(
                    id='counties-dpdn',
                    options=[],
                    value=[],
                    # value='Fertility rate, total (births per woman)',
                ),
            ],
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'}
        ),

        # Vigilância
        html.Hr(style={'display': 'inline-block', 'float': 'left', 'width': '100%'}),
        html.H2(children='Vigilância'),
        html.Div(
            children=[
                dcc.Graph(id='graphic-cloro'),
            ],
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'},
        ),
        html.Div(
            children=[
                dcc.Graph(id='graphic-turb'),
            ],
            style={'display': 'inline-block', 'float': 'left', 'width': '48%'},
        ),
    ]
)


@app.callback(
    Output('counties-dpdn', 'options'),
    Output('counties-dpdn', 'value'),
    Input('dd-municipio', 'value'),
    prevent_initial_call=True
)
def get_formas_abastecimento(id_ibge):
    # Paths
    user = 'open-geodata'
    repo = 'br_sisagua'
    branch = 'master'
    path = 'data/output/{}/dados brutos/vigilancia/vigilancia_parametros_basicos.xlsx'.format(id_ibge)
    url_csv = os.path.join('https://raw.githubusercontent.com', user, repo, branch, path)
    url_csv = url_csv.replace(' ', '%20')

    # Read Dataframe
    df = pd.read_excel(
        url_csv,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
        ]
    )
    # Results
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == 'SAA']
    counties_of_states = [{'label': c, 'value': c} for c in sorted(df['Nome Da Forma De Abastecimento'].unique())]
    values_selected = [x['value'] for x in counties_of_states]
    return counties_of_states, values_selected


@app.callback(
    Output('graphic-cloro', 'figure'),
    Input('dd-municipio', 'value'),
    Input('counties-dpdn', 'value'),
    prevent_initial_call=True
)
def graph_vig_cloro(id_ibge, forma_abastecimento):
    # Paths
    user = 'open-geodata'
    repo = 'br_sisagua'
    branch = 'master'
    path = 'data/output/{}/dados brutos/vigilancia/vigilancia_parametros_basicos.xlsx'.format(id_ibge)
    url_csv = os.path.join('https://raw.githubusercontent.com', user, repo, branch, path)
    url_csv = url_csv.replace(' ', '%20')

    # Read Dataframe
    df = pd.read_excel(
        url_csv,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    # print(df['Parâmetro (Parâmetros Básicos)'].unique())
    # df = df.loc[df['Tipo Da Forma De Abastecimento'] == 'SAA']
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cloro')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df.loc['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

    # Adjust Dates
    df['Data Da Coleta'] = pd.to_datetime(df['Data Da Coleta'])

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


@app.callback(
    Output('graphic-turb', 'figure'),
    Input('dd-municipio', 'value'),
    Input('counties-dpdn', 'value'),
    prevent_initial_call=True
)
def graph_vig_turbidez(id_ibge, forma_abastecimento):
    # Paths
    user = 'open-geodata'
    repo = 'br_sisagua'
    branch = 'master'
    path = 'data/output/{}/dados brutos/vigilancia/vigilancia_parametros_basicos.xlsx'.format(id_ibge)
    url_csv = os.path.join('https://raw.githubusercontent.com', user, repo, branch, path)
    url_csv = url_csv.replace(' ', '%20')

    # Read Dataframe
    df = pd.read_excel(
        url_csv,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == 'SAA']
    print(df['Parâmetro (Parâmetros Básicos)'].unique())
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Turbidez (uT)')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df.loc['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

    # Adjust Dates
    df['Data Da Coleta'] = pd.to_datetime(df['Data Da Coleta'])

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
        title='Turbidez (uT) na "{}"'.format(forma_abastecimento),
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
        # debug=True,
        # port=8050,
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
