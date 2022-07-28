#!/usr/bin/env python
# coding: utf-8


from open_geodata import geo




def convert_6d_to_7d(df, del_municipios_name=True):
    """
    Converte as colunas "id_ibge" de 6 dígitos
    para o código padrão com 7 dígitos.

    O nome do município, se tiver no dataframe,
    é deletado!
    :param df:
    :param del_municipios_name:
    :return:
    """
    # Get Dataframe com nomes
    df_mun_geo = geo.load_dataset('tab_municipio_nome')
    df_mun_geo['id_ibge_6d'] = df_mun_geo['id_municipio'].astype(str).str[0:6].astype(int)

    # Merge
    df = df_mun_geo.merge(
        df,
        left_on='id_ibge_6d',
        right_on='id_ibge'
    )

    # Deleta Colunas
    df.drop(
        ['id_ibge', 'id_ibge_6d', 'municipio'],
        inplace=True,
        axis=1,
        errors='ignore'
    )
    if del_municipios_name:
        df.drop(
            ['municipio_nome'],
            inplace=True,
            axis=1,
            errors='ignore'
        )

    # Rename Colunas
    df.rename({'id_municipio': 'id_ibge'}, axis=1, inplace=True, )
    return df


def adjust_id_ibge(id_ibge):
    """
    Corrigi o valor do código IBGE para o padrão observado no Siságua, ou seja, com apenas 6 dígitos.
    :type id_ibge: object
    :rtype: object
    """
    len_ibge = len(str(id_ibge))
    if len_ibge == 6:
        print('Padrão IBGE antigo, com código de 6 dígitos.\nSem correções necessárias.')
        id_ibge_adjusted = int(id_ibge)
        print('Código IBGE: {}'.format(id_ibge_adjusted))

    elif len_ibge == 7:
        print('Padrão IBGE novo, com código de 7 dígitos.\nCorreções necessárias aplicadas!')
        id_ibge_adjusted = int(id_ibge[0:6])
        print('Código IBGE: {}'.format(id_ibge_adjusted))

    else:
        print('Padrão Diferente!\nDesenvolver correção!')

    return id_ibge_adjusted


def find_states(id_ibge):
    id_estado = int(id_ibge[0:2])
    df = geo.load_dataset('tab_ufs_ibge')
    df = df[df['id'] == id_estado]
    return df.to_dict('records')[0]


if __name__ == '__main__':
    # São Carlos
    codigo_ibge = '3548906'

    # Ajusta Código
    codigo_ibge_ajustado = adjust_id_ibge(codigo_ibge)
    # print(codigo_ibge_ajustado)

    # df = geo.load_dataset('tab_ufs_ibge')
    # print(df.head())
    # print(df.dtypes)

    a = find_states(codigo_ibge)
    print(a)
    print(type(a))
