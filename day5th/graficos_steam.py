import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
# pip install streamlit

st.title("Visualização dos Dados")

# Upload do Arquivo CSV
arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

# Verificar se o arquivo existe
if arquivo is not None:
    # Ler o arquivo
    df = pd.read_csv(arquivo)

    st.write("Dados carregados:")
    st.dataframe(df)

    # Selectbox - para tipo de gráfico
    opcao = st.selectbox(
    "Escolha o tipo de gráfico: ",
    ["Barras", "Pizza", "Linha"])

    # Gráfico de Barras
    if opcao == "Barras":
        st.bar_chart(df.set_index("Nome")["Quantidade"])

    # Gráfico de Pizza
    elif opcao == "Pizza":
        st.pyplot(df.set_index("Nome").plot.pie(y="Quantidade").figure)

else:
    st.info("Envie um arquivo CSV com as colunas Nome e Quantidade...")

# python -m streamlit run graficos_steam.py