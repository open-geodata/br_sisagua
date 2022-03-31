#!/usr/bin/env python
# coding: utf-8


import os
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

# Parameters
id_ibge = '3526902'  # Limeira

# Paths
output_path_dados = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..', '..',
        'data',
        'output',
    )
)

print(output_path_dados)

df = pd.read_excel(
    os.path.join(output_path_dados, str(id_ibge), 'vigilancia', 'vigilancia_parametros_basicos.xlsx')
)

# Results
print(df.info())

# Select Parameters
df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cloro')]

# Ajusta Resultados
df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
df.loc['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')
df.head()

# Adjust Dates
df['Data Da Coleta'] = pd.to_datetime(df['Data Da Coleta'])
df['Data Do Laudo'] = pd.to_datetime(df['Data Do Laudo'])
df['Data De Registro No Sisagua'] = pd.to_datetime(df['Data De Registro No Sisagua'])

# Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

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
            y=df[df['Nome Da Forma De Abastecimento'] == xaxis_column_name]['Resultado'],
            name='conclusao',
            mode='markers',
            marker={'color': 'red'},
            opacity=0.8,
        )
    )

    # Update
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
    return fig


if __name__ == '__main__':
    app.run_server(
        debug=True
    )
