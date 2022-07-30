"""
sss
"""

from ..packages import *

# Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand('Siságua', href='/'),
            dbc.NavbarToggler(id='id_navbar_toggler'),
            dbc.Collapse(
                dbc.Nav(
                    [
                        # dbc.NavItem(dbc.NavLink('Link', href='#')),
                        # dbc.NavLink('Cadastro', href='/cadastro', active='exact'),
                        # dbc.NavLink('Home', href='/', active='exact'),
                        dbc.DropdownMenu(
                            label='Cadastro',
                            nav=True,
                            in_navbar=True,
                            children=[
                                dbc.DropdownMenuItem('Pontos de Captação', href='/cadastro_captacoes'),
                                dbc.DropdownMenuItem('População Abastecida', href='/cadastro_populacao'),
                                dbc.DropdownMenuItem('Tratamento de Água', href='/cadastro_tratamento'),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label='Vigilância',
                            nav=True,
                            in_navbar=True,
                            children=[
                                dbc.DropdownMenuItem('Parâmetros Básicos', href='/vig_param_basicos'),
                                dbc.DropdownMenuItem('Demais Parâmetros', href='/vig_param_outros'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Cianobactérias e Cianotoxinas', href='/vig_ciano'),
                            ],
                        ),
                        dbc.DropdownMenu(
                            label='Controle',
                            nav=True,
                            in_navbar=True,
                            children=[
                                dbc.DropdownMenuItem('Parâmetros Básicos', href='/controle_param_basicos'),
                                dbc.DropdownMenuItem('Demais Parâmetros', href='/controle_param_outros'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Infraestrutura Operacional', href='/controle_infra'),
                                dbc.DropdownMenuItem(divider=True),
                                dbc.DropdownMenuItem('Amostras Fora do Padrão', href='/controle_param_fora'),
                                dbc.DropdownMenuItem('Parâmetros Semestrais', href='/controle_semestral'),
                            ],
                        ),
                    ],
                    class_name='ms-auto',
                    navbar=True,
                    pills=True,
                ),
                id='id_navbar_collapse',
                navbar=True,
            ),
        ]
    ),
    className='mb-5',
)
