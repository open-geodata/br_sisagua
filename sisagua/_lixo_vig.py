#!/usr/bin/env python
# coding: utf-8


import os
import platform
import sys
import pandas as pd
#from src.sisagua.git_api import *
#from src.sisagua.municipio import *
from dash import Dash, dcc, html, Input, Output


def set_url(id_ibge):
    """

    :type id_ibge: object
    """
    if platform.node() in ('michel-vbox'):
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..',
                '..',
                'data',
                'output',
                str(id_ibge),
                'dados brutos',
                'vigilancia',
                'vigilancia_parametros_basicos.xlsx'
            )
        )

    else:
        user = 'open-geodata'
        repo = 'br_sisagua'
        branch = 'master'
        path = os.path.join(
            'data',
            'output',
            '{}'.format(id_ibge),
            'dados brutos',
            'vigilancia',
            'vigilancia_parametros_basicos.xlsx'
        )
        url_git = os.path.join(
            'https://raw.githubusercontent.com',
            user,
            repo,
            branch,
            path
        )
        return url_git.replace(' ', '%20')


if __name__ == '__main__':
    # Parameters
    id_ibge = '3526902'  # Limeira
    url = set_url(id_ibge)
    print(url)



@app.callback(
    Output(component_id='intermediate-value-vig', component_property='data'),
    Input(component_id='municipio', component_property='value'),
    Input(component_id='tipo-abastecimento', component_property='value'),
    Input(component_id='formas-abastecimento', component_property='value'),
    Input(component_id='param-basic-vig', component_property='value'),
    prevent_initial_call=True
)
def vig_get_param_other_amostras(
        id_ibge,
        forma_abastecimento_tipo,
        forma_abastecimento_nome,
        parametro,
):
    if forma_abastecimento_nome is None or parametro is None:
        # PreventUpdate prevents ALL outputs updating
        raise dash.exceptions.PreventUpdate

    # Tabela
    dict_row = df_param_basic_vig[df_param_basic_vig['parametro_campo'] == parametro].to_dict('records')[0]
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









