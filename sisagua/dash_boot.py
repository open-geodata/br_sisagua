import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.graph_objects as go

from graphs import *
from page_home import *
from page_cadastro import *
from page_vigilancia import *
from page_controle import *
from basic_parameters import *
from bitio import *

# Themes
url_theme1 = dbc.themes.CERULEAN
url_theme2 = dbc.themes.SOLAR

# Initial Data
# list_municipios =

# Aplication
app = Dash(
    __name__,
    external_stylesheets=[
        url_theme1,
        url_theme2,
        'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css'
    ],
    title='Siságua',
)

# Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand('Siságua', href='/'),
            dbc.NavbarToggler(id='navbar-toggler1'),
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
                id='navbar-collapse1',
                navbar=True,
            ),
        ]
    ),
    className='mb-5',
)

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
                            id='municipio',
                            options=[],
                            placeholder='Selecione o município',
                        ),
                    ]
                ),

                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Tipo de Abastecimento'),
                        dbc.RadioItems(
                            id='cad-tipo-abastecimento',
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

                html.Div(id='add-fields'),
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
                                themes=[url_theme1, url_theme2]
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

# Content
# the styles for the main content position it to the right of the sidebar and
# add some padding.
content = html.Div(
    id='page-content',
    style={
        'margin-left': '18rem',
        'margin-right': '2rem',
        'padding': '2rem 1rem',
    }
)

# App
app.layout = html.Div(
    [
        navbar,
        dcc.Location(id='url'),
        sidebar,
        content,

        # dcc.Store stores the intermediate value
        dcc.Store(id='vig-basic-data-json'),
        dcc.Store(id='vig-other-data-json'),
        dcc.Store(id='con-basic-data-json'),
    ]
)














@app.callback(
    Output(component_id='page-content', component_property='children'),
    Output(component_id='add-fields', component_property='children'),
    Output(component_id='municipio', component_property='options'),
    Input(component_id='url', component_property='pathname')
)
def render_pages(pathname):
    """

    :rtype: object
    :param pathname:
    :return:
    """
    print(pathname)
    if pathname == '/':
        content = home_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/cadastro_captacoes':
        content = cad_captacao_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/cadastro_populacao':
        content = cad_populacao_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/cadastro_tratamento':
        content = cad_tratamento_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/vig_param_basicos':
        content = vig_basic_page

        add_fields = html.Div(
            [
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Forma de Abastecimento'),
                        dbc.Select(
                            id='vig-basic-forma-abastecimento',
                            options=[],
                            placeholder='Selecione o Forma',
                        ),
                    ],
                ),
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Parâmetros'),
                        dbc.Select(
                            id='vig-basic-param',
                            options=[],
                            placeholder='Selecione Parâmetro',
                        ),
                    ]
                )
            ]
        ),


        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/vig_param_outros':
        content = vig_other_page
        add_fields = html.Div(
            [
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Forma de Abastecimento'),
                        dbc.Select(
                            id='vig-other-forma-abastecimento',
                            options=[],
                            placeholder='Selecione o Forma',
                        ),
                    ],
                ),
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Parâmetros'),
                        dbc.Select(
                            id='vig-other-param',
                            options=[],
                            placeholder='Selecione Parâmetro',
                        ),
                    ]
                )
            ]
        ),
        list_municipios = get_vig_other_parameters_municipio()
        return content, add_fields, list_municipios

    elif pathname == '/vig_ciano':
        content = vig_ciano_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios



    elif pathname == '/controle_param_basicos':
        content = controle_parameters_basic



        add_fields = html.Div(
            [
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Forma de Abastecimento'),
                        dbc.Select(
                            id='con-basic-forma-abastecimento',
                            options=[],
                            placeholder='Selecione o Forma',
                        ),
                    ],
                ),
                html.Div(
                    [
                        html.Hr(style={'margin-top': '30px'}),
                        dbc.Label('Parâmetros'),
                        dbc.Select(
                            id='con-basic-param',
                            options=[],
                            placeholder='Selecione Parâmetro',
                        ),
                    ]
                )
            ]
        ),




        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/controle_param_outros':
        content = con_other_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/controle_infra':
        content = con_infra_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/controle_param_fora':
        content = con_fora_padrao_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    elif pathname == '/controle_semestral':
        content = con_semestral_page
        add_fields = None
        list_municipios = get_cadastro_municipios_municipios()
        return content, add_fields, list_municipios

    # If the user tries to reach a different page, return a 404 message
    content = html.Div(
        dbc.Container(
            [
                html.H1('404: Not found', className='text-danger'),
                html.Hr(),
                html.P(f'The pathname {pathname} was not recognised...'),
            ],
            fluid=True,
            className='py-3',
        ),
        className='p-3 bg-light rounded-3',
    )
    add_fields = None
    list_municipios = get_cadastro_municipios_municipios()
    return content, add_fields, list_municipios














@app.callback(
    Output(component_id='cad-tipo-abastecimento', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    prevent_initial_call=True,
)
def cad_get_forma_abastecimento_tipo(id_ibge):
    """

    :param id_ibge:
    :return:
    :rtype: object
    """
    # Query
    sql = f'''
        SELECT DISTINCT "forma_abastecimento_tipo" FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
        WHERE "id_ibge" = {id_ibge};
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {'id_ibge': id_ibge})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df.head())
    return [
        {'label': row['forma_abastecimento_tipo'],
         'value': row['forma_abastecimento_tipo']}
        for i, row in df.iterrows()
    ]










@app.callback(
    Output(component_id='cad-forma-abastecimento', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    prevent_initial_call=True
)
def cad_get_forma_abastecimento_nome(id_ibge, forma_abastecimento_tipo):
    # Query
    sql = f'''
        SELECT DISTINCT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df.head())

    return [
        {
            'label': row['forma_abastecimento_nome'],
            'value': row['forma_abastecimento_nome']} for i, row in df.iterrows()
    ]






def cad_get_captacoes(id_ibge):
    """
    Busca parâmetros da Vigilância Sanitária com base na tabela do python
    :param id_ibge:
    :return:
    :rtype: object
    """
    return 1








@app.callback(
    Output(component_id='vig-basic-param', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    prevent_initial_call=True,
)
def vig_basic_get_param(id_ibge):
    """
    Busca parâmetros da Vigilância Sanitária com base na tabela do python
    :param id_ibge:
    :return:
    :rtype: object
    """
    return [
        {
            'label': '{} ({})'.format(
                row['parametro_descricao'],
                row['unidade']
            ),
            'value': row['parametro_campo']
        } for i, row in df_vig_basic_param.iterrows()
    ]


















@app.callback(
    Output(component_id='vig-basic-forma-abastecimento', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    prevent_initial_call=True,
)
def vig_basic_get_forma_abastecimento_nome(id_ibge, forma_abastecimento_tipo):
    """

    :param id_ibge:
    :return:
    :rtype: object
    """
    # Query
    sql = f'''
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_bacterias"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_cloro_combinado"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_cloro_livre"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'        
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_coliformes"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'        
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_cor"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'        
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_di_cloro"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'        
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_e_coli"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'        
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_fluor"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_turbidez"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_par_basico_ph"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df.head())

    return [
        {'label': row['forma_abastecimento_nome'],
         'value': row['forma_abastecimento_nome']}
        for i, row in df.iterrows()
    ]





























@app.callback(
    Output(component_id='vig-basic-data-json', component_property='data'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    Input(component_id='vig-basic-forma-abastecimento', component_property='value'),
    Input(component_id='vig-basic-param', component_property='value'),
    prevent_initial_call=True
)
def vig_basic_get_amostras(
        id_ibge,
        forma_abastecimento_tipo,
        forma_abastecimento_nome,
        parametro,
):
    if forma_abastecimento_nome is None or parametro is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate

    # Tabela
    dict_row = df_vig_basic_param[df_vig_basic_param['parametro_campo'] == parametro].to_dict('records')[0]
    TABLE = dict_row['tabela_db']

    # Query
    sql = f'''
        SELECT * FROM "{USERNAME}/{REPO}"."{TABLE}"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "forma_abastecimento_nome" = '{forma_abastecimento_nome}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo,
            'forma_abastecimento_nome': forma_abastecimento_nome,
        })

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df)
    return df.to_json(date_format='iso', orient='split')


















@app.callback(
    Output(component_id='vig-basic-graphic', component_property='figure'),
    Input(component_id='vig-basic-data-json', component_property='data'),
    Input(component_id='vig-basic-forma-abastecimento', component_property='value'),
    Input(component_id='vig-basic-param', component_property='value'),
)
def vig_basic_get_graph(datajson, forma_abastecimento_nome, parametro):
    # Prevent Update prevents ALL outputs updating
    if forma_abastecimento_nome is None or parametro is None:
        raise dash.exceptions.PreventUpdate

    #
    dict_row = df_vig_basic_param[df_vig_basic_param['parametro_campo'] == parametro].to_dict('records')[0]
    parametro_desc = '{} ({})'.format(
        dict_row['parametro_descricao'],
        dict_row['unidade']
    )

    # Data
    df = pd.read_json(datajson, orient='split')

    if len(df) == 0:
        return graph_no_data(
            parametro=dict_row['parametro_descricao'],
            forma_abastecimento_nome=forma_abastecimento_nome,
        )

    else:
        return graph_vig_basic(
            x=df['data_coleta'],
            y=df['resultado'],
            parametro=parametro_desc,
            forma_abastecimento_nome=forma_abastecimento_nome,
        )








@app.callback(
    Output(component_id='vig-other-param', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    Input(component_id='vig-other-forma-abastecimento', component_property='value'),
    prevent_initial_call=True
)
def vig_other_get_param(
        id_ibge,
        forma_abastecimento_tipo,
        forma_abastecimento_nome,
):
    # Query
    sql = f'''
        SELECT "parametro" FROM "{USERNAME}/{REPO}"."vig_demais_parametros"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "forma_abastecimento_nome" = '{forma_abastecimento_nome}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo,
            'forma_abastecimento_nome': forma_abastecimento_nome,
        })
    df = pd.DataFrame(query.fetchall())
    print(df)
    if len(df) == 0:
        # TODO: Botar uma anotação mencionando haver zero amostras
        return [{'label': 'Sem Demais Parâmetros', 'value': 'Sem Demais Parâmetros'}]
    else:
        return [{'label': i, 'value': i} for i in list(set(df['parametro']))]












@app.callback(
    Output(component_id='vig-other-forma-abastecimento', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    prevent_initial_call=True,
)
def vig_other_get_forma_abastecimento_nome(id_ibge, forma_abastecimento_tipo):
    """

    :param id_ibge:
    :return:
    :rtype: object
    """
    # Query
    sql = f'''
        SELECT DISTINCT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."vig_demais_parametros"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df.head())

    return [
        {'label': row['forma_abastecimento_nome'],
         'value': row['forma_abastecimento_nome']}
        for i, row in df.iterrows()
    ]





















@app.callback(
    Output(component_id='vig-other-data-json', component_property='data'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    Input(component_id='vig-other-forma-abastecimento', component_property='value'),
    Input(component_id='vig-other-param', component_property='value'),
    prevent_initial_call=True
)
def vig_other_get_amostras(
        id_ibge,
        forma_abastecimento_tipo,
        forma_abastecimento_nome,
        parametro,
):
    if forma_abastecimento_nome is None or parametro is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate

    # Tabela
    #dict_row = df_param_basic_vig[df_param_basic_vig['parametro_campo'] == parametro].to_dict('records')[0]
    #TABLE = dict_row['tabela_db']

    # Query
    sql = f'''
        SELECT * FROM "{USERNAME}/{REPO}"."vig_demais_parametros"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        AND "forma_abastecimento_nome" = '{forma_abastecimento_nome}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo,
            'forma_abastecimento_nome': forma_abastecimento_nome,
        })

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df.head())
    return df.to_json(date_format='iso', orient='split')



















@app.callback(
    Output(component_id='vig-other-graphic', component_property='figure'),
    Input(component_id='vig-other-data-json', component_property='data'),
    Input(component_id='vig-other-forma-abastecimento', component_property='value'),
    Input(component_id='vig-other-param', component_property='value'),
)
def vig_other_get_graph(
        datajson,
        forma_abastecimento_nome,
        parametro
):
    """

    :param datajson:
    :param forma_abastecimento_nome:
    :param parametro:
    :return:
    :rtype: object
    """
    # Prevent Update prevents ALL outputs updating
    if forma_abastecimento_nome is None or parametro is None:
        raise dash.exceptions.PreventUpdate

    df = pd.read_json(datajson, orient='split')
    print(df[['parametro', 'resultado']].head())
    if len(df) == 0:
        return graph_no_data(
            parametro=parametro,
            forma_abastecimento_nome=forma_abastecimento_nome,
        )

    else:
        return graph_vig_basic(
            x=df['data_coleta'],
            y=df['resultado'],
            parametro=parametro,
            forma_abastecimento_nome=forma_abastecimento_nome,
        )











@app.callback(
    Output(component_id='con-basic-param', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    prevent_initial_call=True
)
def con_basic_get_param(id_ibge):
    """
    Busca parâmetros do Controle com base na tabela do python
    :param id_ibge:
    :return:
    :rtype: object
    """

    return [
        {
            'label': '{} ({})'.format(
                row['parametro_descricao'],
                row['unidade']
            ),
            'value': row['parametro_campo']
        } for i, row in df_con_basic_param.iterrows()
    ]








@app.callback(
    Output(component_id='con-basic-forma-abastecimento', component_property='options'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    prevent_initial_call=True,
)
def con_basic_get_forma_abastecimento_nome(id_ibge, forma_abastecimento_tipo):
    """

    :param id_ibge:
    :return:
    :rtype: object
    """
    # Query
    # TODO: Ajuster query adicionando tabelas
    sql = f'''
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."con_basics_cloro_livre"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."con_basics_bacterias"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'        
        UNION
        SELECT "forma_abastecimento_nome" FROM "{USERNAME}/{REPO}"."con_basics_cloro_combinado"
        WHERE "id_ibge" = {id_ibge}
        AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}';
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql), {
            'id_ibge': id_ibge,
            'forma_abastecimento_tipo': forma_abastecimento_tipo})

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    print(df.head())

    return [
        {'label': row['forma_abastecimento_nome'],
         'value': row['forma_abastecimento_nome']}
        for i, row in df.iterrows()
    ]














@app.callback(
    Output(component_id='con-basic-data-json', component_property='data'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='cad-tipo-abastecimento', component_property='value'),
    Input(component_id='con-basic-forma-abastecimento', component_property='value'),
    Input(component_id='con-basic-param', component_property='value'),
    prevent_initial_call=True
)
def con_basic_get_amostras(
        id_ibge,
        forma_abastecimento_tipo,
        forma_abastecimento_nome,
        parametro,

):
    # Prevent Update prevents ALL outputs updating
    if forma_abastecimento_nome is None or parametro is None:
        raise dash.exceptions.PreventUpdate

    # Tabela
    dict_row = df_con_basic_param[df_con_basic_param['parametro_campo'] == parametro].to_dict('records')[0]
    TABLE = dict_row['tabela_db']

    # Query
    sql = f'''
                SELECT * FROM "{USERNAME}/{REPO}"."{TABLE}"
                WHERE "id_ibge" = {id_ibge}
                AND "forma_abastecimento_tipo" = '{forma_abastecimento_tipo}'
                AND "forma_abastecimento_nome" = '{forma_abastecimento_nome}';
            '''
    print(sql)

    # Execute
    try:
        with engine.connect() as conn:
            conn.execution_options(autocommit=True)
            query = conn.execute(text(sql), {
                'id_ibge': id_ibge,
                'forma_abastecimento_tipo': forma_abastecimento_tipo,
                'forma_abastecimento_nome': forma_abastecimento_nome,
            })

        # Dataframe
        df = pd.DataFrame(query.fetchall())
    except Exception as e:
        print(e)
        df = pd.DataFrame()
    print(df)
    return df.to_json(date_format='iso', orient='split')











@app.callback(
    Output(component_id='con-basic-graphic', component_property='figure'),
    Input(component_id='con-basic-data-json', component_property='data'),
    Input(component_id='con-basic-forma-abastecimento', component_property='value'),
    Input(component_id='con-basic-param', component_property='value'),
)
def con_basic_get_graph(datajson, forma_abastecimento_nome, parametro):
    # Prevent Update prevents ALL outputs updating
    if forma_abastecimento_nome is None or parametro is None:
        raise dash.exceptions.PreventUpdate

    # Read Parameters
    dict_row = df_con_basic_param[df_con_basic_param['parametro_campo'] == parametro].to_dict('records')[0]
    parametro_desc = '{} ({})'.format(
        dict_row['parametro_descricao'],
        dict_row['unidade']
    )

    # Read Dataframe
    try:
        df = pd.read_json(datajson, orient='split')
        print(df[['parametro', 'resultado']].head())
    except Exception as e:
        print(e)
        return graph_error_query(
        parametro=parametro,
        forma_abastecimento_nome=forma_abastecimento_nome,
    )

    if len(df) == 0:
        return graph_no_data(
            parametro=parametro,
            forma_abastecimento_nome=forma_abastecimento_nome,
        )

    else:
        # TODO: Ajustar gráfico com stack Ano e Mês
        return graph_vig_basic(
            x=df['mes_referencia'],
            y=df['resultado'],
            parametro=parametro_desc,
            forma_abastecimento_nome=forma_abastecimento_nome
        )










if __name__ == '__main__':
    app.run_server(
        # debug=True,
        # port=8050,
    )
