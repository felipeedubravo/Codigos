import matplotlib.pyplot as plt
import pandas as pd

# Lendo o arquivo de dados preparado
df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\visualizacao_dados\clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras (Abordagem 1: usando o plot do próprio Pandas)
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee90')
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

# Extraindo os dados para a segunda abordagem
x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

# Gráfico de Barras (Abordagem 2: usando o plt.bar do Matplotlib)
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#66aa65')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.show()

# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
plt.show()

# Gráfico de Dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Oranges')

# CORREÇÃO: Cria a colorbar e define o label separadamente
cbar = plt.colorbar()
cbar.set_label('Contagem dentro do bin')

plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

#Gráfico de Dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap="Blues")
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

#Criar o gráfico de pizza
plt.figure(figsize=(8, 8))

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas

# https://matplotlib.org/stable/users/explain/colors/colormaps.html

