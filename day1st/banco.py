print("Bem vindo ao Banco 171")
saldo = float(input("Digite seu saldo... R$"))

transferencia = float(input("Qual o valor da transferencia? R$"))

# valide se ela possui saldo suficiente para a transferencia
# Estrutura de Decisão

if saldo >= transferencia:
    print("Saldo suficiente!")
    # Atualizando valor do saldo 
    saldo = saldo - transferencia   
    print("Seu saldo atual é de R$", saldo)
else: 
    print("Saldo não é suficiente")
    