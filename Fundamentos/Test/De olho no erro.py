import pandas as pd

data = pd.read_csv('dados.csv')
# Verificando valores nulos
print(data.isnull().sum())
# Tratando valores nulos
data = data.dropna()
print(data.head())