import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df= pd.read_csv('clientes-v2-tratados.csv')

linhas = 250
print(df.head())
print('-' * linhas)

# Transformação Logaritmica
df["salario_Log"] = np.log1p(df['salario']) #Logipe usado para evitar problemas com valores zero

print("\nDataFrame após transformação logaritmica no salario':\n", df.head())
print('-' * linhas)

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario']+1)

print("\nDataFrame após transformação Box-Cox no salario':\n", df.head())
print('-' * linhas)

#Codificação de Frequência para Testado!
estado_freq = df['estado'].value_counts() / len(df)
df['estado freq'] = df['estado'].map(estado_freq)
print("\nDataFrame após codificação de frequência para estado:\n", df.head())
print('-' * linhas)

#Interações
df['interacan_idade_filhos'] = df['idade'] = df['numero_filhos']
print("\nDataFrame após criação de interações entre idade' e 'numero filhos':\n", df.head())