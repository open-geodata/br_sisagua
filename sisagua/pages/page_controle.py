#!/usr/bin/env python
# coding: utf-8

from dash import dcc, html
import dash_bootstrap_components as dbc




controle_parameters_basic = html.Div(
    children=[
        html.Div(
            className='row seven columns',
            children=dcc.Graph(id='con-basic-graphic'),
        ),
        html.Div(
            className='row two columns',
            children="""
            Art. 32 É obrigatória a manutenção de, no mínimo, 0,2 mg/L de cloro residual livre ou 2 mg/L de cloro residual combinado ou de 0,2 mg/L de dióxido de cloro em toda a extensão do sistema de distribuição (reservatório e rede) e nos pontos de consumo.
            """,
        ),
    ],
)


con_other_page = dbc.Label('Desenvolver página e análises'),
con_infra_page = dbc.Label('Desenvolver página e análises'),
con_fora_padrao_page = dbc.Label('Desenvolver página e análises'),
con_semestral_page = dbc.Label('Desenvolver página e análises'),
