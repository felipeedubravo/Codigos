import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max.colwidth', None)

# Lembre-se de ajustar este caminho se o FileNotFoundError persistir
df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\estatistica_dados/clientes-v3-preparado.csv')
linhas = 250
print(df.head())
print('-' * linhas)
print(df)
print('-' * linhas)
print('Estatistica com Pandas')
print('-' * linhas)
print('Média:', df['salario'].mean())
print('-' * linhas)
print('Mediana:', df['salario'].median())
print('-' * linhas)
print('Variância:', df['salario'].var())
print('-' * linhas)
print('Desvio Padrão:', df['salario'].std())
print('-' * linhas)
print('Moda:', df['salario'].mode()[0])
print('-' * linhas)
print('Minimo: ', df['salario'].min())
print('-' * linhas)
print('Quartis:\n', df['salario'].quantile([0.25, 0.5, 0.75]))
print('-' * linhas)
print('Máximo:', df['salario'].max())
print('-' * linhas)
print('Contagem de não nulos:', df['salario'].count())
print('-' * linhas)
print('Soma:', df['salario'].sum())
print('-' * linhas)

# Estrutura de dados
print("Coluna do Dataframe:\n", df['salario'])
print('-' * linhas)
print("Array do campo: ", df['salario'].values)

print('-' * linhas)
print('Estatistica com Numpy')
print('-' * linhas)
print("Média com coluna:", np.mean(df['salario']))
print('-' * linhas)
print("Média com array:", np.mean(df['salario'].values))

array_campo = df['salario'].values
print("Mediana:", np.median(array_campo))
print("Variância:", np.var(array_campo))

pt = print()

print(pt)