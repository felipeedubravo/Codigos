import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\visualizacao_dados\clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograms
# Gera um histograma rápido e sem formatação da coluna 'salario' (salário)
plt.hist(df['salario'])
plt.show()

# Histograms - Parameters
# Define o tamanho da figura como 10 polegadas de largura por 6 polegadas de altura.
plt.figure(figsize=(10, 6))

# Plota o histograma com 100 bins, barras verdes e 60% de opacidade
plt.hist(df['salario'], bins=100, color='green', alpha=0.6)

# Adicionando títulos e rótulos em português
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')

# Define marcas de escala personalizadas no eixo X, de 0 até o salário máximo, com intervalos de 2000 unidades
plt.xticks(ticks=range(0, int(df['salario'].max()) + 2000, 2000))

plt.ylabel('Frequência')
plt.grid(True) # Adds a background grid
plt.show()

# Múltiplos gráficos
plt.figure(figsize=(10, 6))

# Primeiro subgráfico em um layout de grade 2x2 (Linha 1, Coluna 1, Gráfico 1)
plt.subplot(2, 2, 1) # 2 Linha, 2 Colunas, 1° Gráfico

plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário x Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

# Segunda chamada da grade de subgráficos (parcialmente cortada; parece conter um erro de digitação ou a variação '1, 2, 2')
plt.subplot(1, 2, 2) #1 Linha, 2 Colunas, 2 Gráfico
# Plota 'salario' em relação a 'anos_experiencia' usando um código de cor hexadecimal personalizado
plt.scatter(df['salario'], df['anos_experiencia'], color="#222CB6", alpha=0.6, s=30) # cor hexadecimal online
# plt.title('Dispersão - Idade x Anos de Experiência') [Truncado]
plt.title('Dispersão - Salário x Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de Calor (Correlação)
corr = df[['salario', 'anos_experiencia']].corr()

# 2º Gráfico: Heatmap (Linha 1, Colunas 2, Posição 2)
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout() # Ajusta o espaçamento entre os gráficos
plt.show()