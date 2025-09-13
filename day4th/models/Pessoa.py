
class Pessoa:
    
    # definição
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastar(self):
        print("Cadastrando pessoa...")

    def sair(self):
        print("Saindo do sistema...")
        