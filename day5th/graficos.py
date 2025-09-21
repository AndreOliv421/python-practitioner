import pandas as pd
import matplotlib.pyplot as plt

#
#

ARQUIVO = "produtos.csv"
CAMPOS = ["Nome", "Quantidade", "Preco"]

df =pd.read_csv(ARQUIVO, encoding="utf-8")

df["Faturamento"] = df["Quantidade"] * df["Preco"]
print(df)

df.boxplot(column="Preco", by="Produto", grid=True)
plt.title("Distribuição de Preco por Produto")
plt.xlabel("Preco")
plt.ylabel("Nome")

plt.show()



df.plot(kind="bar", x="Nome", y="Preco", grid=True)
plt.title("Preco dos Produtos")
plt.xlabel("Nome")
plt.ylabel("Preco")

plt.show()
