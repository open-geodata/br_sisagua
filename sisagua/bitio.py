#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text




USERNAME = 'michelmetran'
REPO = 'br_sisagua'
API_KEY = '3iZAb_9h6ucvXkPMCZBkqgCJCHvht'
PASSWORD = 'v2_3svVD_A7YJ4NyMgssmyKxmNgaxYkb'
PG_STRING = f'postgresql://michelmetran_demo_db_connection:{API_KEY}@db.bit.io?sslmode=prefer'
PG_STRING = f'postgresql://michelmetran:v2_3svVD_A7YJ4NyMgssmyKxmNgaxYkb@db.bit.io/michelmetran/br_sisagua'
PG_STRING = f'postgresql://{USERNAME}:{PASSWORD}@db.bit.io/{USERNAME}/{REPO}'

engine = create_engine(PG_STRING, isolation_level='AUTOCOMMIT')


def get_cadastro_municipios_municipios():
    # Query
    sql = f'''
        SELECT "id_ibge", "municipio_nome" FROM "{USERNAME}/{REPO}"."cadastro_municipios";
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql))

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    return [{'label': row['municipio_nome'], 'value': row['id_ibge']} for i, row in df.iterrows()]


def get_vig_other_parameters_municipio():
    """
    Seleciona Municípios que tem alguma amostra em "vig_demais_parametros"
    :rtype: object
    """
    # Query
    sql = f'''
        SELECT tab1."id_ibge", tab1."municipio_nome" FROM "{USERNAME}/{REPO}"."cadastro_municipios" AS tab1
        INNER JOIN (
          SELECT DISTINCT "id_ibge"
          FROM "{USERNAME}/{REPO}"."vig_demais_parametros") AS tab2
        ON tab1.id_ibge = tab2.id_ibge
        ORDER BY tab1."id_ibge";
    '''
    print(sql)

    # Execute
    with engine.connect() as conn:
        conn.execution_options(autocommit=True)
        query = conn.execute(text(sql))

    # Dataframe
    df = pd.DataFrame(query.fetchall())
    return [{'label': row['municipio_nome'], 'value': row['id_ibge']} for i, row in df.iterrows()]


# def get_formas(id_ibge):
#     # Query
#     sql = f'''
#         SELECT * FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
#         WHERE "id_ibge" = {id_ibge};
#     '''
#     print(sql)
#
#     # Execute
#     with engine.connect() as conn:
#         conn.execution_options(autocommit=True)
#         query = conn.execute(text(sql), {'id_ibge': id_ibge})
#
#     # Dataframe
#     df = pd.DataFrame(query.fetchall())
#     print(df)
#     return df

#
# def get_df_vig_cloro_livre(id_ibge):
#     # TODO: Arrumar isso e entender pra que serve, e se serve!
#     # Query
#     sql = f'''
#         SELECT * FROM "{USERNAME}/{REPO}"."cadastro_formas_instituicoes"
#         WHERE "id_ibge" = {id_ibge};
#     '''
#     print(sql)
#
#     # Execute
#     with engine.connect() as conn:
#         conn.execution_options(autocommit=True)
#         query = conn.execute(text(sql), {'id_ibge': id_ibge})
#
#     # Dataframe
#     df = pd.DataFrame(query.fetchall())
#     print(df)
#     return df


if __name__ == '__main__':
    id_ibge = 3501301
    # a = get_municipios()
    # print(a)
    # get_formas(id_ibge)
