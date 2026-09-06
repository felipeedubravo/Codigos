import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

















# 1. Leitura dos Dados e Configuração
sns.set_theme(style="whitegrid")
df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\Pratique\ecommerce_estatistica.csv')

# 2. Gráfico de Histograma (Distribuição de Preços)
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Preço', bins=20, color='skyblue', kde=True)
plt.title('Distribuição dos Preços dos Produtos', fontsize=14)
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Frequência (Quantidade)', fontsize=12)
plt.show()

# 3. Gráfico de Dispersão (Avaliações vs. Quantidade Vendida)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='N_Avaliações', y='Qtd_Vendidos_Cod', color='purple', alpha=0.6)
plt.title('Relação entre Número de Avaliações e Vendas', fontsize=14)
plt.xlabel('Número de Avaliações', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.show()

# 4. Mapa de Calor (Correlação entre Variáveis Numéricas)
plt.figure(figsize=(8, 6))
colunas_num = df[['Qtd_Vendidos_Cod', 'N_Avaliações', 'Preço', 'Nota', 'Desconto']]
sns.heatmap(colunas_num.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Mapa de Calor: Correlações Numéricas', fontsize=14)
plt.show()

# 5. Gráfico de Barra (Quantidade de Produtos por Gênero)
plt.figure(figsize=(10, 6))
# Adicionado hue='Gênero' e legend=False para resolver o FutureWarning
sns.countplot(data=df, x='Gênero', hue='Gênero', order=df['Gênero'].value_counts().index, palette='viridis', legend=False)
plt.title('Quantidade de Produtos por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.show()

# 6. Gráfico de Pizza (Participação por Temporada)
plt.figure(figsize=(8, 8))
contagem_temporada = df['Temporada'].value_counts()
plt.pie(contagem_temporada, labels=contagem_temporada.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Distribuição de Produtos por Temporada', fontsize=14)
plt.show()

# 7. Gráfico de Densidade (Concentração das Notas)
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Nota', fill=True, color='orange')
plt.title('Densidade das Notas de Avaliação', fontsize=14)
plt.xlabel('Nota (0 a 5)', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.show()

# 8. Gráfico de Regressão (Impacto do Desconto nas Vendas)
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Desconto', y='Qtd_Vendidos_Cod', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Tendência: Impacto do Desconto nas Vendas', fontsize=14)
plt.xlabel('Desconto Concedido (%)', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.show()