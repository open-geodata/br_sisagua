"""
sss
"""


from ..packages import *


vig_basic_page = html.Div(
    children=[
        html.Div(
            className='row seven columns',
            children=dcc.Graph(id='id_vig_basic_graphic'),
        ),
        html.Div(
            className='row two columns',
            children="""
            Art. 32 É obrigatória a manutenção de, no mínimo, 0,2 mg/L de cloro residual livre ou 2 mg/L de cloro residual combinado ou de 0,2 mg/L de dióxido de cloro em toda a extensão do sistema de distribuição (reservatório e rede) e nos pontos de consumo.
            """,
        ),
    ],
)


vig_other_page = html.Div(
    children=[
        html.Div(
            className='row seven columns',
            children=dcc.Graph(id='id_vig_other_graphic'),
        ),
        html.Div(
            className='row two columns',
            children="""
            Art. 32 É obrigatória a manutenção de, no mínimo, 0,2 mg/L de cloro residual livre ou 2 mg/L de cloro residual combinado ou de 0,2 mg/L de dióxido de cloro em toda a extensão do sistema de distribuição (reservatório e rede) e nos pontos de consumo.
            """,
        ),
    ],
)


vig_ciano_page = html.Div(
    dbc.Label('Desenvolver página e análises')
)
