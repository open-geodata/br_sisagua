#!/usr/bin/env python
# coding: utf-8

from open_geodata import geo


def adjust_id_ibge(id_ibge):
    len_ibge = len(str(id_ibge))
    if len_ibge == 6:
        print('Padrão IBGE antigo, com código de 6 dígitos.\nSem correções necessárias.')
        id_ibge = int(id_ibge)
        print('Código IBGE: {}'.format(id_ibge))

    elif len_ibge == 7:
        print('Padrão IBGE novo, com código de 7 dígitos.\nCorreções necessárias aplicadas!')
        id_ibge = id_ibge[0:6]
        id_ibge = int(id_ibge)
        print('Código IBGE: {}'.format(id_ibge))

    else:
        print('Padrão Diferente!\nDesenvolver correção!')

    return id_ibge


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
    #print(codigo_ibge_ajustado)
    
    #df = geo.load_dataset('tab_ufs_ibge')
    #print(df.head())
    #print(df.dtypes)
    

    a = find_states(codigo_ibge)
    print(a)
    print(type(a))
