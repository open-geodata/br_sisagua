"""
sss
"""


from ..packages import *
from ..styles.style import url_theme1, url_theme2


# Sidebar
sidebar = html.Div(
    [
        html.B(
            'Controles',
            # className='display-4'
        ),
        dbc.Nav(
            [
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Município'),
                        dbc.Select(
                            id='id_municipio',
                            options=[],
                            placeholder='Selecione o município',
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Tipo de Abastecimento'),
                        html.Br(),
                        dbc.Button(
                            id='id_submit_button',
                            n_clicks=0,
                            children='Listar',
                            color='primary',
                            style={
                                'textAlign': 'center',
                                'margin-botton': '30px'
                            },
                        ),
                        dbc.RadioItems(
                            id='id_cad_tipo_abastecimento',
                            options=[
                                {'label': 'SAA', 'value': 'SAA'},
                                {'label': 'SAC', 'value': 'SAC'},
                                {'label': 'SAI', 'value': 'SAI'}
                            ],
                            # value='SAA',
                            inline=True,
                        ),
                    ]
                ),
                html.Div(id='id_add_fields'),
            ],
            vertical=True,
            pills=True,
        ),

        html.Div(
            [
                html.Hr(style={'margin-top': '30px'}),
                dbc.Row(
                    [
                        dbc.Col(dbc.Label('Tema')),
                        dbc.Col(
                            ThemeSwitchAIO(
                                aio_id='theme',
                                themes=[url_theme2, url_theme1]
                            ),
                        ),
                    ],
                    align='end',
                ),
            ]
        ),
    ],
    style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '16rem',
        'padding': '4rem 1rem 2rem',
        'background-color': '#f8f9fa',
    },
)
