
class Cliente:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    # Ao invés de exibir o código da memória, exibe o texto abaixo
    def __str__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, idade={self.idade})"
            