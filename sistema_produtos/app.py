from flask import Flask, request, render_template, redirect

import csv, os

app = Flask(__name__)

ARQUIVO = 'dados.csv'

def inicializar_csv():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Nome", "Email", "Produto", "Quantidade"])
def ler_registros():
    inicializar_csv()
    with open(ARQUIVO, 'r', newline="", encoding="utf-8") as sarquivo:
        reader = csv.reader(ARQUIVO)
        return list(reader)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        produto = request.form["produto"]
        quantidade = request.form["quantidade"]

        with open(ARQUIVO, 'a', newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([nome, email, produto, quantidade])

    registros = ler_registros()
    return render_template("index.html", registros=registros)
if __name__ == "__main__":
    inicializar_csv()
    app.run(debug=True)
