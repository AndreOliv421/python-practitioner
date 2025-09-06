
class Carro:

    # Configuração inicial do objeto
    def __init__(self, marca, modelo, nome, cor, ano):
        # Definir atributo
        self.cor = marca
        self.modelo = modelo
        self.nome = nome
        self.cor = cor
        self.an0 = ano

    def ligar(self):
        print("Ligando o carro........", self.nome)

    def acelerar(self):
        print("Acelerando muito.......")
    
    def frear(self):
        print("Freiando.... Discos super aquecidos")

opalaCarro = Carro("Chevrolet", "6cc", "Opala", "Preto", "1978")
opalaCarro.ligar()

opalaCarro.acelerar()
opalaCarro.frear()

