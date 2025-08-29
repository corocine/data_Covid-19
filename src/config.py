import pandas as pd    # Manipulação de dados em tabelas
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
file_path = os.path.join(BASE_DIR, "data", "caso_full.csv")

df = pd.read_csv(file_path)
# print(df.head(5))

# TRADUÇÕES
columns_translated = {
    "city": "cidade",
    "city_ibge_code": "código_ibge_cidade",
    "date": "data",
    "epidemiological_week": "semana_epidemiológica",
    "estimated_population": "população_estimada",
    "estimated_population_2019": "população_estimada_2019",
    "is_last": "é_último",
    "is_repeated": "é_repetido",
    "last_available_confirmed": "confirmados_acumulados",
    "last_available_confirmed_per_100k_inhabitants": "confirmados_por_100mil_habitantes",
    "last_available_date": "data_última_atualização",
    "last_available_death_rate": "taxa_letalidade",
    "last_available_deaths": "óbitos_acumulados",
    "order_for_place": "ordem_local",
    "place_type": "tipo_local",
    "state": "estado",
    "new_confirmed": "novos_casos",
    "new_deaths": "novos_óbitos"
}

locale_type_translated = {
    'city': 'cidade',
    'state': 'estado'
}

is_last_translated = {
    'True': 'verdadeiro',
    'False': 'falso'
}

is_repeated_translated = {
    'true': 'verdadeiro',
    'false': 'falso'
}

# RENOMEAR CONFORME TRADUÇÃO
df.rename(columns=columns_translated, inplace=True) # Renomear colunas com rename
df['tipo_local'] = df['tipo_local'].replace(locale_type_translated) # Renomear campos com replace
df['é_último'] = df['é_último'].replace(is_last_translated) # Renomear campos com replace
df['é_repetido'] = df['é_repetido'].replace(is_repeated_translated) # Renomear campos com replace


# print(df.columns)
# print(df.head(5))

# print(df.isnull().sum()) # descobrir onde existem campos nulos
# print(df[df.isnull().any(axis=1)]) # Exibir as linhas que contenham valores nulos
# print(df['cidade'].unique()) # descobrir quais valores existem no campo 

df = df.assign(código_ibge_cidade=df['código_ibge_cidade'].astype('Int64'))
df = df.assign(população_estimada=df['população_estimada'].astype('Int64'))
df = df.assign(população_estimada_2019=df['população_estimada_2019'].astype('Int64'))


# Descoberta dos dados

# print(df.columns)
# print(df.head(5))
# print(df.describe(include=['object'])) # análise de dados com texto ou categórico.
# print(df['população_estimada'].unique())

print(df.isna().sum().sort_values(ascending=False))

print(df.isna().any(axis=1).sum()) #axis=1 → opera por linha | axis=0 → opera por coluna

print((df.isna().sum() / len(df)).sort_values(ascending=False) * 100) # Verificar se valores nulos são maiores que 5% da base


df_clean = df.dropna()

file_path = os.path.join(BASE_DIR, "data", "clean_caso_full.csv")

df_clean.to_csv(file_path, index=False)
print('Limpeza concluída! Arquivo gerado está na pasta data/cleanData.csv')




