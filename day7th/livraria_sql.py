import sqlite3

conn = sqlite3.connect("livros.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano INTEGER
    )
''')

# loop principal
while True:
    print("=== CADASTRO DE LIVROS ===")
    print("1 - Cadastrar novo Livro")
    print("2 - Listar Livros")
    print("3 - Sair")

    opcao = input("Escolha uma opção...")

    if opcao == "1":
        titulo = input("Titulo do livro: ")
        autor = input("Autor: ")
        ano = int(input("Ano de publicacao: "))

        cursor.execute("INSERT INTO livro (titulo, autor, ano) VALUES (?, ?, ?)", (titulo, autor, ano))

        conn.commit()  # confirmar inserção de dados
        print(f'Livro {titulo} criado com sucesso!')
    elif opcao == "2":
        print("Livros cadastrados")
        for linha in cursor.execute("SELECT * FROM livros"):
            print(f'ID: {linha[0]} | Titulo {linha[1]} | Autor {linha[2]} | Ano {linha[3]}')
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opcao Invalida, tente novamente...")
