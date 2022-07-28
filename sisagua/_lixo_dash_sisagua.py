#!/usr/bin/env python
# coding: utf-8


import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
# from src.sisagua.git_api import *
# from src.sisagua.vig import *
from src.sisagua.lixo_municipio import *
#from src.sisagua.lixo_vig import set_url
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from bitio import *

list_municipios = get_cadastro_municipios_municipios()

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

                #
                html.Div('Selecione um município:'),
                dcc.Dropdown(
                    id='dd-municipio',
                    options=list_municipios,
                    # value='3501608',
                    placeholder='Selecione um município',
                    # value='Fertility rate, total (births per woman)',
                ),
                html.Br(),

                #
                html.Div('Selecione um Ano:'),
                dcc.Dropdown(
                    id='opt-ano-referencia',
                    options=[],
                    # value='3501608',
                    placeholder='Selecione um Ano',
                    # value='Fertility rate, total (births per woman)',
                ),
                html.Br(),

                #
                html.Div('Selecione o Tipo de Abastecimento:'),
                dcc.RadioItems(
                    options=['SAA', 'SAC', 'SAI'],
                    # value='SAA',
                    id='opt-tipo-abastecimento-tipo',
                    inline=True,
                    style={'float': 'center'}
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
                'height': '3500px',
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
                    children="""
                    Art. 32 É obrigatória a manutenção de, no mínimo, 0,2 mg/L de cloro residual livre ou 2 mg/L de cloro residual combinado ou de 0,2 mg/L de dióxido de cloro em toda a extensão do sistema de distribuição (reservatório e rede) e nos pontos de consumo.
                    """,
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
    Output(component_id='opt-ano-referencia', component_property='options'),
    Input(component_id='dd-municipio', component_property='value'),
    prevent_initial_call=True
)
def get_ano_referencia(id_ibge):
    # Query
    sql = f'''
        SELECT DISTINCT "ano_referencia" FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
        WHERE "id_ibge" = {id_ibge};
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {'id_ibge': id_ibge})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    return list(df['ano_referencia'])


@app.callback(
    Output('opt-tipo-abastecimento-tipo', 'options'),
    Input('dd-municipio', 'value'),
    prevent_initial_call=True
)
def get_forma_abastecimento_tipo(id_ibge, ano_referencia):
    # Query
    sql = f'''
        SELECT DISTINCT "forma_abastecimento_tipo" FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
        WHERE "id_ibge" = {id_ibge};
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {'id_ibge': id_ibge})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    return list(df['forma_abastecimento_tipo'])


@app.callback(
    Output('opt-formas-abastecimento', 'options'),
    Output('opt-formas-abastecimento', 'value'),
    Input('dd-municipio', 'value'),
    Input('opt-tipo-abastecimento-tipo', 'value'),
    Input('opt-ano-referencia', 'value'),
    prevent_initial_call=True
)
def get_formas_abastecimento(id_ibge, forma_abastecimento_tipo, ano_referencia):
    # Query
    sql = f'''
        SELECT * FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "ano_referencia" = {ano_referencia};
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(
            text(sql),
            {
                'id_ibge': id_ibge,
                'forma_abastecimento_tipo': forma_abastecimento_tipo,
            }
        )

    # Dataframe
    df = pd.DataFrame(query.fetchall())

    # Results
    options = [{'label': row['forma_abastecimento_nome'], 'value': row['forma_abastecimento_nome']} for i, row in
               df.iterrows()]
    values = [x['value'] for x in options]
    return options, values









@app.callback(
    Output('data-frame', 'data'),
    Input('dd-municipio', 'value'),
    Input('opt-tipo-abastecimento-tipo', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    prevent_initial_call=True
)
def get_vig_amostras(
        id_ibge,
        forma_abastecimento_tipo,
        forma_abastecimento_nome,
):
    # Query
    sql = f'''
        SELECT * FROM "{USERNAME}/{REPO}"."vig_par_basico_cloro_livre"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "forma_abastecimento_nome" = '{forma_abastecimento_nome}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo,
            'forma_abastecimento_nome': forma_abastecimento_nome,
        })

    # Dataframe
    return pd.DataFrame(query.fetchall())




@app.callback(
    Output('graphic-cloro', 'figure'),
    Input('dd-municipio', 'value'),
    Input('opt-tipo-abastecimento-tipo', 'value'),
    Input('opt-ano-referencia', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('opt-formas-abastecimento', 'options'),
    prevent_initial_call=True
)
def graph_vig_cloro_livre(
        id_ibge,
        forma_abastecimento_tipo,
        ano_referencia,
        forma_abastecimento_cod,
        forma_abastecimento_nome,
):
    # Query
    sql = f'''
        SELECT * FROM "{USERNAME}/{REPO}"."vig_par_basico_cloro_livre"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "ano_referencia" = {ano_referencia}
        AND "forma_abastecimento_cod" = '{forma_abastecimento_cod}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo,
            'ano_referencia': ano_referencia,
            'forma_abastecimento_cod': forma_abastecimento_cod,
        })

    # Dataframe
    df = pd.DataFrame(query.fetchall())

    # Create Figure
    fig = go.Figure()

    # Add trace
    fig.add_trace(
        go.Scatter(
            x=df['data_coleta'],
            y=df['resultado'],
            name='conclusao',
            mode='markers',
            marker={'color': 'blue'},
            opacity=0.8,
        )
    )

    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join('Cloro Residual Livre'), 'forma_abastecimento_nome'),
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
    Input('opt-tipo-abastecimento-tipo', 'value'),
    Input('opt-ano-referencia', 'value'),
    Input('opt-formas-abastecimento', 'value'),
    Input('opt-formas-abastecimento', 'options'),
    prevent_initial_call=True
)
def graph_vig_turbidez(
        id_ibge,
        forma_abastecimento_tipo,
        ano_referencia,
        forma_abastecimento_cod,
        forma_abastecimento_nome,
):
    # Query
    sql = f'''
        SELECT * FROM "{USERNAME}/{REPO}"."vig_par_basico_turbidez"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "ano_referencia" = {ano_referencia}
        AND "forma_abastecimento_cod" = '{forma_abastecimento_cod}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo,
            'ano_referencia': ano_referencia,
            'forma_abastecimento_cod': forma_abastecimento_cod,
        })

    # Dataframe
    df = pd.DataFrame(query.fetchall())

    # Create Figure
    fig = go.Figure()

    # Add trace
    fig.add_trace(
        go.Scatter(
            x=df['data_coleta'],
            y=df['resultado'],
            name='conclusao',
            mode='markers',
            marker={'color': 'blue'},
            opacity=0.8,
        )
    )

    # Update
    fig.update_layout(
        title='{}<br><sup>{}</sup>'.format(' '.join('Turbidez'), 'forma_abastecimento'),
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
