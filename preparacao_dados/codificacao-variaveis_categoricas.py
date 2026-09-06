import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

linhas = 250
print(df.head())
print('-' * linhas)

#Codificação one-hot para 'estado_civil
df = pd.concat( [df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1) # concat e para concatena
print("\nDataFrame após codificação one-hot para 'estado_civil':\n", df.head())
print('-' * linhas)

#Codificação ordinal para 'nivel educacao
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel educacao_ordinal'] = df ['nivel_educacao'].map(educacao_ordem)
print("\nDataFrame após codificação ordinal para 'nivel_educacao:\n", df.head())
print('-' * linhas)

#Transformar Varea_atuacao em categorías codificadas usando o método.cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print("\nDataFrame após transformar 'area_atuacao' em códigos numéricos: \n", df.head())
print('-' * linhas)

#LabelEncoder para estado
#LabelEncoder converte cada valor único em números de 8 an_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])
print("\nDataFrame após aplicar LabelEncoder em estado':\n", df.head())