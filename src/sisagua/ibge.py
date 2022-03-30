#!/usr/bin/env python
# coding: utf-8



def adjust_cod_ibge(cod_ibge):
    if len(str(cod_ibge)) == 6:
        print('Padrão IBGE antigo, com código de 6 dígitos.\nSem correções necessárias.')
        cod_ibge = int(cod_ibge)
        print('Código IBGE: {}'.format(cod_ibge))

    elif len(str(cod_ibge)) == 7:
        print('Padrão IBGE novo, com código de 7 dígitos.\nCorreções necessárias aplicadas!')
        cod_ibge = cod_ibge[0:6]
        cod_ibge = int(cod_ibge)
        print('Código IBGE: {}'.format(cod_ibge))

    else:
        print('Padrão Diferente!\nDesenvolver correção!')
        
    return cod_ibge




if __name__ == '__main__':
    # São Carlos
    cod_ibge = '3548906' 

    # Ajusta Código
    adjust_cod_ibge(cod_ibge)
