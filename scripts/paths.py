"""
Pastas do Projeto
julho de 2023
"""


from pathlib import Path


project_path = Path(__file__).parents[1]


# Pastas
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

docs_path = project_path / 'docs'
docs_path.mkdir(exist_ok=True)

# Bruto
bruto_path = data_path / 'brutos'
bruto_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

input_path_parquet = input_path / 'parquet'
input_path_parquet.mkdir(exist_ok=True)

input_path_parquet_partitioned = input_path / 'parquet_partitioned'
input_path_parquet_partitioned.mkdir(exist_ok=True)

output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)


# Bruto
# import os
# output_path_cidades = os.path.join(output_path, 'cidades')

# Cria
# os.makedirs(bruto_path, exist_ok=True)
# os.makedirs(input_path, exist_ok=True)
# os.makedirs(output_path, exist_ok=True)

# Inputs
# os.makedirs(input_path_parquet, exist_ok=True)
# os.makedirs(input_path_parquet_partitioned, exist_ok=True)

# Cria
# os.makedirs(output_path_cidades, exist_ok=True)

# controle_path = os.path.join(bruto_path, 'controle')
# vigilancia_path = os.path.join(bruto_path, 'vigilancia')
# os.makedirs(cadastro_path, exist_ok=True)
# os.makedirs(controle_path, exist_ok=True)
# os.makedirs(vigilancia_path, exist_ok=True)
#
# project_path = Path(__file__).parents[1].resolve()
#
# data_path = project_path / 'data'
# data_path.mkdir(exist_ok=True)
#
# input_path = data_path / 'input'
# input_path.mkdir(exist_ok=True)
#
# output_path = data_path / 'output'
# output_path.mkdir(exist_ok=True)


if __name__ == '__main__':
    print(project_path)
