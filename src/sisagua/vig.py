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
