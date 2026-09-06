import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

df = pd.read_csv(r'C:\Users\Usuario\PycharmProjects\estatistica_dados/clientes-v3-preparado.csv')

#Categorizar salario: acima e abaixo da mediana
df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int)
# 1 - acima da mediana, O abaixo ou igual a mediana

X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']]

Y = df['salario_categoria'] # Prever

#Dividir dados: Treinamento e Toste
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42)

#Criar e treinar modelo - modelo Regressão Logistica
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

#Criar e treinar modelo Arvore de Decisão
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

#Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_test)
Y_prev_dt = modelo_dt.predict(X_test)

#Métricas de avaliação Regressão Logística
accuracy_lr = accuracy_score(Y_test, Y_prev_lr)
precision_lr = precision_score (Y_test, Y_prev_lr)
recall_lr = recall_score(Y_test, Y_prev_lr)

linhas = 250
print('-' * linhas)
print(f"\nAcurácia da Regressão Logistica: {accuracy_lr:.2f}")

print(f"Precisão da Regressão Logistica: {precision_lr:.2f}")

print(f"Recall (Sensibilidade) da Regressão Logistica: {recall_lr:.2f}")
print('-' * linhas)

# Métricas de avaliação Arvore de Decisão
accuracy_dt = accuracy_score(Y_test, Y_prev_dt)
precision_dt = precision_score(Y_test, Y_prev_dt)
recall_dt = recall_score (Y_test, Y_prev_dt)

print(f"\nAcurácia da Árvore de Decisão: {accuracy_dt:.2f}")

print(f"Precisão da Árvore de Decisão: {precision_dt:.2f}")

print(f"Recall (Sensibilidade) da Árvore de Decisão: {recall_dt:.2f}")
print('-' * linhas)

#Salvar modelo treinado
joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkl')
joblib.dump(modelo_dt, 'modelo_arvore_decisao.pkl')