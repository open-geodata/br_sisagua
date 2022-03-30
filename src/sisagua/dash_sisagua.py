#!/usr/bin/env python
# coding: utf-8

import os
import sys
#import folium
#import numpy as np
import pandas as pd
#import seaborn as sns
#import geopandas as gpd
#from folium import plugins
from datetime import date


try:
    print('Read "ibge" from Python File')
    from ibge import *
except:
    pass


try:
    print('Read "paths" from Jupyter')
    from paths import *
    
except:
    print('Não deu pra importar paths')


# Parameters
estado = 'SP'
cod_ibge = '3548906' # São Carlos
cod_ibge = '3526902' # Limeira

# Adjust Code
cod_ibge_adjusted = adjust_cod_ibge(cod_ibge)

# Path name
city_path = '{}_{}'.format(estado, cod_ibge_adjusted)
city_path


try:
    print('Read "data" from Python File')
    output_path_cidades = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'output', 'cidades'))
    df = pd.read_excel(
        os.path.join(output_path_cidades, city_path, 'vigilancia', 'vigilancia_parametros_basicos.xlsx')
    )
except:
    pass


# Results
print(df.info())


# Select Parameters
df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cloro')]


# Ajusta Resultados
df['Resultado'] = df['Resultado'].astype(str).str.replace(',','.')
df.loc['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')
df['Resultado']
df.head()


# Adjust Dates
df['Data Da Coleta'] = pd.to_datetime(df['Data Da Coleta'])
df['Data Do Laudo'] = pd.to_datetime(df['Data Do Laudo'])
df['Data De Registro No Sisagua'] = pd.to_datetime(df['Data De Registro No Sisagua'])


import dash
from dash import Dash, dcc, html, Input, Output
from jupyter_dash import JupyterDash


import plotly.express as px
import plotly.graph_objects as go


# Start
app = JupyterDash(__name__)

# 
app.layout = html.Div([
    html.Div([
        html.Div(
            [
                dcc.Dropdown(
                    df['Nome Da Forma De Abastecimento'].unique(),
                    #value='Fertility rate, total (births per woman)',
                    id='xaxis-column'
                ),
            ],
            style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic'),
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
)
def update_graph(xaxis_column_name):
    # Create Figure
    fig = go.Figure()
    
    # Add trace
    fig.add_trace(
        go.Scatter(
            x=df['Data Da Coleta'],
            #y=df['Resultado'],
            y=df[df['Nome Da Forma De Abastecimento'] == xaxis_column_name]['Resultado'],
            name='conclusao',
            mode='markers',
            marker={'color': 'red'},
            opacity=0.8,
        )
    )
    
    # Udate
    fig.update_layout(
        title='Cloro Residual na "{}"'.format(xaxis_column_name),
        xaxis_tickformat='%d %b<br>%Y',
        margin={
            'l': 40,
            'b': 40,
            #'t': 40,
            'r': 0
        },
        #dragmode='pan',
        hovermode='x',

    )
    #fig.write_html('ddd.html', config=config)
    return fig

# Run
app.run_server(mode='inline', port=8051)




