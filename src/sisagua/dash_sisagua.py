#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd


def adjust_cod_ibge(cod_ibge):
    if len(str(cod_ibge)) == 6:
        print('Padrão IBGE antigo, com código de 6 dígitos.\nSem correções necessárias.')
        cod_ibge = int(cod_ibge)
        print('Código IBGE: {}'.format(cod_ibge))

    elif len(str(cod_ibge)) == 7:
        print('Padrão IBGE novo, com código de 7 dígitos.\nCorreções necessárias aplicadas!')
        cod_ibge = cod_ibge[0:6]
        cod_ibge = int(cod_ibge)
        print('Código IBGE: {}'.format(cod_ibge))

    else:
        print('Padrão Diferente!\nDesenvolver correção!')

    return cod_ibge


# Parameters
estado = 'SP'
cod_ibge = '3526902'  # Limeira

# Adjust Code
cod_ibge_adjusted = adjust_cod_ibge(cod_ibge)

# Path name
city_path = '{}_{}'.format(estado, cod_ibge_adjusted)

print('Read "data" from Python File')
output_path_cidades = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..', '..',
        'data', 'output',
        'cidades'
    )
)

print(output_path_cidades)

# 'https://raw.githubusercontent.com/open-geodata/br_sisagua/data/output/cidades/SP_352690/vigilancia/vigilancia_parametros_basicos.xlsx'
df = pd.read_excel(
    os.path.join(output_path_cidades, city_path, 'vigilancia', 'vigilancia_parametros_basicos.xlsx')
)

# Results
print(df.info())

# Select Parameters
df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cloro')]

# Ajusta Resultados
df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
df.loc['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')
df['Resultado']
df.head()

# Adjust Dates
df['Data Da Coleta'] = pd.to_datetime(df['Data Da Coleta'])
df['Data Do Laudo'] = pd.to_datetime(df['Data Do Laudo'])
df['Data De Registro No Sisagua'] = pd.to_datetime(df['Data De Registro No Sisagua'])

import dash
from dash import Dash, dcc, html, Input, Output
# from jupyter_dash import JupyterDash

import plotly.express as px
import plotly.graph_objects as go

# Start
app = Dash(__name__)

# 
app.layout = html.Div([
    html.Div([
        html.Div(
            [
                dcc.Dropdown(
                    df['Nome Da Forma De Abastecimento'].unique(),
                    # value='Fertility rate, total (births per woman)',
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
            # y=df['Resultado'],
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
            # 't': 40,
            'r': 0
        },
        # dragmode='pan',
        hovermode='x',

    )
    # fig.write_html('ddd.html', config=config)
    return fig


if __name__ == '__main__':
    app.run_server(
        debug=True
    )
