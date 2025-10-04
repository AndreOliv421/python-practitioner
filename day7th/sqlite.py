import sqlite3

conn = sqlite3.connect('alunos.db')
cursos = conn.cursor()

# cria uma tabela se não existir

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TXT
    nota REAL
)
''')

# inserir dados
cursor.execute('INSERT INTO alunos (nome, nota) VALUES (?, ?)', ('Andre', 8.0))
conn.commit() # Executor

# Consular os dados
for row in cursor.execute("SELECT * FROM alunos"):
    print(row)

conn.close()