"""
sss
"""


from ..packages import *


home_page = html.Div(
    [
        dbc.Container(
            [
                html.H1('Sobre', className='text-primary'),
                html.Hr(),
                html.P(
                    'Com objetivo de facilitar analises dos dados de qualidade de água tratada dos municípios do Estado de São Paulo, foi desenvovido o presente dashboard.',
                    className='lead'
                ),
                html.P('Apresenta a descrição do sistema de abastecimento público, conforme preenchimento das Vigilâncias Sanitárias Municipais e outros responsáveis.', className='lead'),
                html.P(
                    'Avaliar o atendimento a Portaria do Ministério da Saúde nº 05, de 2017.', className='lead'),
            ],
            fluid=True,
            className='py-3',
        ),
        dbc.Row(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4('Dados', className='card-title'),
                            # html.H6('Autor', className='card-subtitle'),
                            html.P(
                                'Os dados do Siságua foram obtidos por meio do Portal de Dados Abertos, do Governo Federal, em fevereiro de 2022',
                                className='card-text',
                            ),
                            dbc.CardLink(
                                'Portal de Dados Abertos',
                                href='https://dados.gov.br/dataset?tags=SISAGUA',
                                target='_blank'
                            ),
                        ]
                    ),
                    style={'width': '18rem'},
                    className='p-3 bg-light rounded-3',
                ),
                html.Br(),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4('Autor', className='card-title'),
                            # html.H6('Autor', className='card-subtitle'),
                            html.P(
                                'Esse projeto foi desenvolvido por Michel Metran, Assessor do Ministério Público do Estado de São Paulo, visando facilitar análises ambientais',
                                className='card-text',
                            ),
                            dbc.CardLink(
                                'LinkedIn',
                                href='https://www.linkedin.com/in/michelmetran/',
                                target='_blank'
                            ),
                            dbc.CardLink(
                                'GitHub',
                                href='https://github.com/michelmetran',
                                target='_blank'
                            ),
                        ]
                    ),
                    style={'width': '18rem'},
                    className='p-3 bg-light rounded-3',
                ),
                html.Br(),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4('Python', className='card-title'),
                            # html.H6('Autor', className='card-subtitle'),
                            html.P(
                                'Empregando conhecimentos de python, foi possível:\n'
                                '- Obter os dados;'
                                '- Corrigi-los;'
                                '- Carrega-los em um banco de dados relacional;',
                                '- Elaborar esse dashboard.',
                                className='card-text',
                            ),
                            dbc.CardLink(
                                'Repositório',
                                href='https://github.com/open-geodata/br_sisagua',
                                target='_blank'
                            ),
                        ]
                    ),
                    style={'width': '18rem'},
                    className='p-3 bg-light rounded-3',
                ),
            ]
        ),
    ],
)

