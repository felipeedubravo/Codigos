import pandas as pd

# Carregando os dados
df = pd.read_csv('/data/ecommerce_tratados.csv')

# 1. Verificar a quantidade de dados únicos para cada campo
# Dica: Use o método que retorna o número de valores únicos por coluna
# Armazene o resultado na variável 'unicos'
unicos = df.nunique()

# 2. Verificar as estatísticas dos campos numéricos
# Dica: Use o método que gera estatísticas descritivas (média, desvio, min, max, etc.)
# Armazene o resultado na variável 'estatisticas'
estatisticas = df.describe()

# 3. Criar o campo 'Preco' com o cálculo: Reais + (Centavos/100)
# Dica: Acesse as colunas 'Reais' e 'Centavos' do DataFrame
# Lembre-se de dividir os centavos por 100 para converter para formato decimal
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# 4. Remover os seguintes campos: ['Reais', 'Centavos', 'Condicao', 'Condicao_Atual']
# Dica: Use o método drop() com o parâmetro columns
# Não esqueça de atribuir o resultado de volta ao DataFrame
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])

# Verificação dos resultados - NÃO ALTERE ESTA PARTE
print("Dados Únicos por Campo:")
print(unicos)

print("\nEstatísticas dos Campos Numéricos:")
print(estatisticas)

print("\nDataFrame após as alterações:")
print(df.head())