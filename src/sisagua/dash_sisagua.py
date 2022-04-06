#!/usr/bin/env python
# coding: utf-8


import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
# from src.sisagua.git_api import *
# from src.sisagua.vig import *
from src.sisagua.municipio import *
from src.sisagua.vig import set_url

# Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(
    __name__,
    title='Siságua',
    external_stylesheets=external_stylesheets
)
server = app.server

# Divs
app.layout = html.Div(
    children=[
        # Header
        html.Div(
            className='three columns',
            children=[
                html.H1('Siságua', style={'text-align': 'left'}),
                html.P('Painel construído com dados do Siságua, obtidos no Portal de Dados Abertos.'),
                html.P('Elaborando visando avaliar o atendimento a Portaria MS 05/17'),
                html.Br(),
                html.P('Michel Metran da Silva'),
                html.A('Repositório', href='https://github.com/open-geodata/br_sisagua'),
                html.Hr(),
                html.H2('Opções'),
                html.Div('Selecione um município:'),
                dcc.Dropdown(
                    id='dd-municipio',
                    options=list_cities,
                    #value='3501608',
                    placeholder='Selecione um município utilizando o código IBGE',
                    # value='Fertility rate, total (births per woman)',
                ),
                html.Br(),
                html.Div('Selecione o Tipo de Abastecimento:'),
                dcc.RadioItems(
                    options=['SAA', 'SAC', 'SAI'],
                    value='SAA',
                    id='radio-tipo-abastecimento',
                    inline=True,
                    style={
                        'float': 'center'
                    }
                ),
                html.Br(),
                html.Div('Selecione uma Forma de Abastecimento:'),
                dcc.Dropdown(
                    id='opt-formas-abastecimento',
                    options=[],
                    value=[],
                ),
            ],
            style={
                # 'display': 'inline-grid',
                'position': 'relative',
                'height': '3000px',
                'background-color': 'lightgrey',
            },
        ),

        # Gráficos
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-cloro'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-turb'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-fluor'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-ecoli'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-cor'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-coliformes'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    className='row seven columns',
                    children=dcc.Graph(id='graphic-ph'),
                ),
                html.Div(
                    className='row two columns',
                    children=['Informações sobre o gráfico\n' * 10],
                ),
            ],
        ),
    ]
)


# style={'display': 'inline-block', 'float': 'left', 'width': '48%'}

@app.callback(
    Output('opt-formas-abastecimento', 'options'),
    Output('opt-formas-abastecimento', 'value'),
    Input('dd-municipio', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def get_formas_abastecimento(id_ibge, tipo_abastecimento):
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
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    counties_of_states = [{'label': c, 'value': c} for c in sorted(df['Nome Da Forma De Abastecimento'].unique())]
    values_selected = [x['value'] for x in counties_of_states]
    return counties_of_states, values_selected


@app.callback(
    Output('graphic-cloro', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_cloro(id_ibge, forma_abastecimento, tipo_abastecimento):
    # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cloro')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))

    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_turbidez(id_ibge, forma_abastecimento, tipo_abastecimento):
    # # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Turbidez')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))
    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
    Output('graphic-fluor', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_fluor(id_ibge, forma_abastecimento, tipo_abastecimento):
    # # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Fluoreto')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))
    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
    Output('graphic-ecoli', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_ecoli(id_ibge, forma_abastecimento, tipo_abastecimento):
    # # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Escherichia')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].map({'AUSENTE': 0, 'PRESENTE': 1})

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))
    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
    Output('graphic-cor', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_cor(id_ibge, forma_abastecimento, tipo_abastecimento):
    # # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cor')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))
    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
    Output('graphic-coliformes', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_coliformes(id_ibge, forma_abastecimento, tipo_abastecimento):
    # # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Coliformes')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].map({'AUSENTE': 0, 'PRESENTE': 1})

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))
    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
    Output('graphic-ph', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('radio-tipo-abastecimento', 'value'),
    prevent_initial_call=True
)
def graph_vig_ph(id_ibge, forma_abastecimento, tipo_abastecimento):
    # # Paths
    url = set_url(id_ibge)

    # Read Dataframe
    df = pd.read_excel(
        url,
        usecols=[
            'Tipo Da Forma De Abastecimento',
            'Nome Da Forma De Abastecimento',
            'Parâmetro (Parâmetros Básicos)',
            'Resultado',
            'Data Da Coleta',
        ]
    )

    # Select Parameters
    df = df.loc[df['Tipo Da Forma De Abastecimento'] == tipo_abastecimento]
    df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('pH')]

    # Ajusta Resultados
    df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
    df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

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
    list_par = list(set(df['Parâmetro (Parâmetros Básicos)']))
    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join(list_par), forma_abastecimento),
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
