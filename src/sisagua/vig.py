#!/usr/bin/env python
# coding: utf-8


import os
import pandas as pd
from src.sisagua.git_api import *
from src.sisagua.municipio import *


# Parameters
id_ibge = '3526902'  # Limeira


# Paths
user = 'open-geodata'
repo = 'br_sisagua'
branch = 'master'
path = 'data/output/{}/dados brutos/vigilancia/vigilancia_parametros_basicos.xlsx'.format(id_ibge)
url_csv = os.path.join('https://raw.githubusercontent.com', user, repo, branch, path)
url_csv = url_csv.replace(' ', '%20')

df = pd.read_excel(
    url_csv,
    usecols=[
        'Nome Da Forma De Abastecimento',
        'Parâmetro (Parâmetros Básicos)',
        'Resultado',
        'Data Da Coleta',
    ]
)

# Results
print(df.info())

# Select Parameters
df = df[df['Parâmetro (Parâmetros Básicos)'].str.contains('Cloro')]

# Ajusta Resultados
df['Resultado'] = df['Resultado'].astype(str).str.replace(',', '.')
df.loc['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')

# Adjust Dates
df['Data Da Coleta'] = pd.to_datetime(df['Data Da Coleta'])
