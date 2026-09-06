import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None) #  configurado a largueara
pd.set_option('display.max_colwidth', None) # maxima da coluna
df = pd.read_csv('clientes-v2-tratados.csv')

linhas = 250
print(df.head())
print('-' * linhas)

#df = df.drop(['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)
df = df[['idade','salario']]

#Normalização MinMaxScaler.
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df [['salario']])

#Padronização StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#Padronização RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(25))