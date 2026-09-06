import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\estatistica_dados/clientes-v3-preparado.csv')

linhas = 250
print('-' * linhas)

#Uso do Pandas
print('Estatistica do dataframe: \n', df.describe())
print('-' * linhas)
print('Estatística formatada:\n', df[['salario', 'idade']].describe().round({'salario': 2, 'idade': 0}))
# minha mudança para ver melhor
print('Estatística formatada:\n', df[['salario', 'idade']].describe().round({'salario': 2, 'idade': 0}).astype({'idade': int}))
print('-' * linhas)
print('Correlação: \n', df[['salario', 'idade' ]].corr())
print('-' * linhas)
print('Correlação com Normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('-' * linhas)
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('-' * linhas)
print('Correlação com Padronização: \n', df [['salarioRobustScaler', 'idadeRobustScaler']].corr())
print('-' * linhas)
print('Correlação: \n', df[[ 'salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())
print('-' * linhas)

# Calcula a matriz de correlação completa entre as duas colunas
correlacao = df[['idade', 'salario']].corr()
print("Matriz de Correlação:\n", correlacao)

print('-' * linhas)
# Para exibir apenas o número exato da correlação formatado para 4 casas decimais:
valor_corr = df['idade'].corr(df['salario'])
print(f"\nA correlação direta entre Idade e Salário é: {valor_corr:.4f}")

import matplotlib.pyplot as plt

# Cria o gráfico de dispersão (scatter plot)
# alpha=0.5 deixa os pontos meio transparentes para vermos onde eles se acumulam
plt.scatter(df['idade'], df['salario'], alpha=0.4, color='blue')

# Adiciona títulos para facilitar a leitura
plt.title('Relação entre Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário (R$)')

# Exibe o gráfico na tela
plt.show()