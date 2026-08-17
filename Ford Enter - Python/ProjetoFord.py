
import pandas as pd

# Use o 'r' antes das aspas e coloque o caminho completo até a planilha
caminho = r"C:\Users\Usuario\Documents\GitHub\Codigos\Ford Enter - Python\projeto_varejo_omnichannel_base_bruta.csv"

df = pd.read_csv(caminho)

print("Base carregada com sucesso!\n\n")
print(df.head())

# print(dataframe_projeto.head().to_string())
print(df.describe(),"\n\n")
print(df.info(),"\n\n")

print(df.shape,"\n\n")
print(df.dtypes,"\n\n")
print(df.columns,"\n\n")

print(df.isnull().sum())

print(df.head())
print(df.tail().to_string())


