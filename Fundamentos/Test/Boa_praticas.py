import pandas as pd # Importa a biblioteca Pandas para manipulação de dados.
from sklearn.preprocessing import StandardScaler, MinMaxScaler #  Importa as classes necessárias para padronização e normalização dos dados.

# Exemplo de DataFrame
data = {'idade': [25, 45, 35, 50],
        'salário': [50000, 100000, 75000, 120000]} # Cria um dicionário com dados de exemplo.


df = pd.DataFrame(data) # Converte o dicionário em um DataFrame do Pandas.

# Padronização
scaler = StandardScaler() # Inicializa o objeto StandardScaler.
df['idade_padronizada'] = scaler.fit_transform(df[['idade']]) # Aplica a padronização na coluna 'idade' e cria uma nova coluna 'idade_padronizada'.
df['salário_padronizado'] = scaler.fit_transform(df[['salário']]) # Aplica a padronização na coluna 'salário' e cria uma nova coluna 'salário_padronizado'.

# Normalização
min_max_scaler = MinMaxScaler() # Inicializa o objeto MinMaxScaler.
df['idade_normalizada'] = min_max_scaler.fit_transform(df[['idade']]) # Aplica a normalização na coluna 'idade' e cria uma nova coluna 'idade_normalizada'.
df['salário_normalizado'] = min_max_scaler.fit_transform(df[['salário']]) # Aplica a normalização na coluna 'salário' e cria uma nova coluna 'salário_normalizado'.

print(df) # Imprime o DataFrame resultante com as novas colunas padronizadas e normalizadas.