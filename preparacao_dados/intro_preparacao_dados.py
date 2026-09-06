#Análise Exploratória de Dados (AED)
import pandas as pd

df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\preparacao_dados\clientes-v2.csv')
linhas = 250

print(df.head().to_string()) # Chama as 5 primeira linha
print('-'*linhas)
print(df.tail().to_string()) # Chama as 5 últimos linha
print('-'*linhas)

# transforma data
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial:')
print('-'*linhas)

print(df.info()) # vai mostra número importante do campo non-null
print('-'*linhas)

print('Analise de dados nulos: \n', df.isnull().sum())
print('-'*linhas)

print('% de dados nulos: \n', df.isnull().mean() * 100)
print('-'*linhas)

df.dropna(inplace=True)
print('Confirmar remoção de dados nulos: ', df.isnull().sum().sum())
print('-'*linhas)
print('Analise de dados duplicados: ', df.duplicated().sum())
print('-'*linhas)
print('Analise de dados únicos:\n', df.nunique())
print('-'*linhas)
print('Estatisticas dos dados: \n', df.describe())
print('-'*linhas)
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())
print('-'*linhas)
df.to_csv('clientes-v2-tratados.csv', index=False)