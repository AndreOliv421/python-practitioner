
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            return True
        else:
            return False
        
    def get_saldo(self):
         return self.saldo
        
contaCliente = ContaBancaria(100)

contaCliente.sacar(50)
contaCliente.depositar(70)

print(contaCliente.get_saldo())

