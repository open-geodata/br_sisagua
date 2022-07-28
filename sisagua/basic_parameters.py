import pandas as pd

df_vig_basic_param = pd.DataFrame(
    [
        {'parametro_campo': 'Cloro residual livre (mg/L)', 'tabela_db': 'vig_par_basico_cloro_livre', 'parametro_descricao': 'Cloro Residual Livre', 'unidade': 'mg/L'},
        {'parametro_campo': 'Cloro residual combinado (mg/L)', 'tabela_db': 'vig_par_basico_cloro_combinado', 'parametro_descricao': 'Cloro Residual Combinado', 'unidade': 'mg/L'},
        {'parametro_campo': 'Dióxido de Cloro (mg/L)', 'tabela_db': 'vig_par_basico_di_cloro', 'parametro_descricao': 'Dióxido de Cloro', 'unidade': 'mg/L'},
        {'parametro_campo': 'Turbidez (uT)', 'tabela_db': 'vig_par_basico_turbidez', 'parametro_descricao': 'Turbidez', 'unidade': 'uT'},
        {'parametro_campo': 'Bactérias Heterotróficas', 'tabela_db': 'vig_par_basico_bacterias', 'parametro_descricao': 'Bactérias Heterotróficas', 'unidade': 'UFC/mL'},
        {'parametro_campo': 'Coliformes totais', 'tabela_db': 'vig_par_basico_coliformes', 'parametro_descricao': 'Coliformes Totais', 'unidade': 'Presença/Ausência'},
        {'parametro_campo': 'Escherichia coli', 'tabela_db': 'vig_par_basico_e_coli', 'parametro_descricao': 'Escherichia coli', 'unidade': 'Presença/Ausência'},
        {'parametro_campo': 'Fluoreto (mg/L)', 'tabela_db': 'vig_par_basico_fluor', 'parametro_descricao': 'Fluoreto', 'unidade': 'mg/L'},
        {'parametro_campo': 'pH', 'tabela_db': 'vig_par_basico_ph', 'parametro_descricao': 'pH', 'unidade': 'Adimensional'},
        {'parametro_campo': 'Cor (uH)', 'tabela_db': 'vig_par_basico_cor', 'parametro_descricao': 'Cor', 'unidade': 'uH'},
    ]
)

df_con_basic_param = pd.DataFrame(
    [
        {'parametro_campo': 'Cloro Residual Livre (mg/L)', 'tabela_db': 'con_basics_cloro_livre', 'parametro_descricao': 'Cloro Residual Livre', 'unidade': 'mg/L'},
        {'parametro_campo': 'Cloro Residual Combinado (mg/L)', 'tabela_db': 'con_basics_cloro_combinado', 'parametro_descricao': 'Cloro Residual Combinado', 'unidade': 'mg/L'},
        {'parametro_campo': 'Dióxido de Cloro', 'tabela_db': 'con_basics_cloro_dioxido', 'parametro_descricao': 'Dióxido de Cloro', 'unidade': 'mg/L'},
        {'parametro_campo': 'Turbidez (uT)', 'tabela_db': 'con_basics_turbidez', 'parametro_descricao': 'Turbidez', 'unidade': 'uT'},
        {'parametro_campo': 'Bactérias Heterotróficas (UFC/mL)', 'tabela_db': 'con_basics_bacterias', 'parametro_descricao': 'Bactérias Heterotróficas', 'unidade': 'UFC/mL'},
        {'parametro_campo': 'Coliformes totais', 'tabela_db': 'con_basics_coliformes_totais', 'parametro_descricao': 'Coliformes Totais', 'unidade': 'Presença/Ausência'},
        {'parametro_campo': 'Escherichia coli', 'tabela_db': 'con_basics_e_coli', 'parametro_descricao': 'Escherichia coli', 'unidade': 'Presença/Ausência'},
        {'parametro_campo': 'Fluoreto (mg/L)', 'tabela_db': 'con_basics_fluor', 'parametro_descricao': 'Fluoreto', 'unidade': 'mg/L'},
        {'parametro_campo': 'pH', 'tabela_db': 'con_basics_ph', 'parametro_descricao': 'pH', 'unidade': 'Adimensional'},
        {'parametro_campo': 'Cor (uH)', 'tabela_db': 'con_basics_cor', 'parametro_descricao': 'Cor', 'unidade': 'uH'},
    ]
)


if __name__ == '__main__':
    print(df_vig_basic_param)
    print(df_con_basic_param)
