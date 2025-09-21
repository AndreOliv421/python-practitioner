import pandas as pd

import matplotlib.pyplot as plt

# pip install matplotlib
# pip install pandas

# ler o arquivo csv 
df_csv = pd.read_csv("dados_pandas.csv")

# Quantidade, Preço
df_filtrado = df_csv[df_csv["Quantidade"] > 5]
print(df_filtrado)

df_ordenado = df_csv.sort_values(by="Quantidade", ascending=False)
print(df_ordenado) # Do maior para o menor (Decrescente)

# Exibir estatisticas
print(df_csv.describe())

# Criar coluna Faturamento
df_csv["Faturamento"] = df_csv["Quantidade"] * df_csv["Preço"]

print(df_csv)

# Vendas
# Camiseta, 70
# Camiseta, 30
# Calculando a média de preço do produto
media_produto = df_csv.groupby("Nome")["Preço"].mean()
print(media_produto)

# Gráfico boxplot
# grid -> linhas
df_csv.boxplot(column="Preço", by="Nome", grid=True)

plt.title("Distribuição de Preço por Produto")
plt.xlabel("Preço")
plt.ylabel("Nome")

plt.show()
