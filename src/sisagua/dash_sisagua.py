#!/usr/bin/env python
# coding: utf-8

import os
import folium
import simplekml
import numpy as np
import pandas as pd
import seaborn as sns
import geopandas as gpd
from folium import plugins
from datetime import date


from paths import *
from cod_ibge import *


# Parameters
estado = 'SP'
cod_ibge = '3548906' # São Carlos
cod_ibge = '3526902' # Limeira

# Adjust Code
cod_ibge_adjusted = adjust_cod_ibge(cod_ibge)

# Path name
city_path = '{}_{}'.format(estado, cod_ibge_adjusted)
city_path


geo_path = os.path.join(output_path_cidades, city_path, 'analysis_geo')
os.makedirs(geo_path, exist_ok=True)


# Read Table
df = pd.read_excel(
    os.path.join(output_path_cidades, city_path, 'vigilancia', 'vigilancia_parametros_basicos.xlsx')
)

# Results
print(df.info())
display(df)


list_cols = ['Região Geográfica', 'Regional De Saúde', 'Município']
df[list_cols].drop_duplicates()


list_cols = [
    'Código Forma De Abastecimento',
    'Tipo Da Forma De Abastecimento',
    'Nome Da Forma De Abastecimento',
]
df[list_cols].drop_duplicates()


list_cols = [
    'Tipo Da Instituição',
    'Sigla Da Instituição',
    'Nome Da Instituição',
    'Cnpj Da Instituição',
    'Nome Do Escritório Regional/Local',
    'Cnpj Do Escritório Regional/Local'
]
df[list_cols].drop_duplicates()


list_cols = [
    'Procedência Da Coleta',
    'Ponto De Coleta',
    #'Área',
    #'Descrição Do Local',
    'Zona',
    'Categoria Área',    
]
df[list_cols].drop_duplicates()


list_cols = [    
    'Zona',
    'Categoria Área',
    'Tipo Do Local',
    'Área',
    'Descrição Do Local',
    'Local',
]
df[list_cols].drop_duplicates()


list_cols = [
    'Latitude',
    'Longitude'
]
df[list_cols].drop_duplicates()


list(df.columns)


list_cols = [
    'Número Da Amostra',
    'Motivo Da Coleta',    
    'Parâmetro (Parâmetros Básicos)',
    'Análise Realizada',
    'Resultado',
    'Providência',
]
df[list_cols].drop_duplicates()


set(df['Análise Realizada'])


set(df['Parâmetro (Parâmetros Básicos)'])


set(df['Parâmetro (Parâmetros Básicos)'])


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


df.dtypes


list(df.columns)


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





import os
from traitlets.config import Config
from nbconvert import PythonExporter
from nbconvert.preprocessors import TagRemovePreprocessor


input_filename = 'jupyter.ipynb'
input_filepath = os.path.join(os.getcwd(), input_filename)
output_filepath = os.path.join(os.getcwd(), 'sss.py')


# Import the exporter
c = Config()
c.TagRemovePreprocessor.enabled=True
c.ClearOutputPreprocessor.enabled=True
c.TemplateExporter.exclude_markdown=True
c.TemplateExporter.exclude_code_cell=False
c.TemplateExporter.exclude_input_prompt=True 
c.TemplateExporter.exclude_output=True
c.TemplateExporter.exclude_raw=True
c.TagRemovePreprocessor.remove_cell_tags = ('remove_cell',)
c.TagRemovePreprocessor.remove_input_tags = ('remove_cell',)
c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
c.preprocessors = ['TagRemovePreprocessor']
c.PythonExporter.preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor']

# Configure and run out exporter
py_exporter = PythonExporter(config=c)
py_exporter.register_preprocessor(TagRemovePreprocessor(config=c), True)

# Configure and run out exporter - returns a tuple - first element with html, second with notebook metadata
body, metadata = PythonExporter(config=c).from_filename(input_filepath)

# Write to output html file
with open(output_filepath,  'w', encoding='utf-8') as f:
    f.write(body)




