import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

linhas = 250
print('-' * linhas)

pd.set_option('display.width', None)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\estatistica_dados/clientes-v3-preparado.csv')

print(df.isnull().sum().sum())
print('-' * linhas)
#Carregar modelo treinado
modelo_regressao_linear = joblib.load('modelo_regressao_linear.pkl')
modelo_regressao_logistica = joblib.load('modelo_regressao_logistica.pkl')
modelo_arvore_decisao = joblib.load('modelo_arvore_decisao.pkl')

#Dados dos novos funcionários
dados_novos_funcionarios = pd.DataFrame({
    'idade': [35, 45,30],
    'anos_experiencia': [6, 12, 5],
    'nivel_educacao_cod': [2, 3, 4], # Ensino Médio, Ensino Superior, Pós-graduação
    'area_atuacao_cod': [1, 4, 3],  #Educação, Tecnologia, Saúde
})


#Prever o salário com modelo treinado
salario_previsto = modelo_regressao_linear.predict(dados_novos_funcionarios)

for x in range(len(salario_previsto)):
    print(F'Salário previsto do {x+1} funcionário: R${salario_previsto[x]:,.2f}')

print('-' * linhas)

#Classificar o salário com modelo treinado
categoria_salario = modelo_regressao_logistica.predict(dados_novos_funcionarios)

for x in range(len(categoria_salario)):
    categoria = 'Acima da mediana' if categoria_salario[x] == 1 else 'Abaixo da mediana'
    print(F'Categoria de salário previsto do {x+1} ^ + funcionário: {categoria}')

df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\estatistica_dados/clientes-v3-preparado.csv')