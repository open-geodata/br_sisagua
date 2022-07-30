"""
sss
"""


from ..packages import *

cad_captacao_page = html.Div(
    className='row two columns',
    children="""
            Desenvolver pagina de cadastro das SAA, SAC e SAI, apresentando uma tabela com as ETAs, bem como uma tabela apresentando informaçoes
            """,
),

cad_populacao_page = html.Div(
    children=[
        html.Div(
            className='row seven columns',
            #children=dcc.Graph(id='vig-basic-graphic'),
        ),
        html.Div(
            className='row two columns',
            children="""
            Apresentar os dados de populaçao.
            """,
        ),
    ],
)

cad_tratamento_page = html.Div(
    children=[
        html.Div(
            className='row seven columns',
            #children=dcc.Graph(id='vig-basic-graphic'),
        ),
        html.Div(
            className='row two columns',
            children="""
            Descrever.
            """,
        ),
    ],
)
