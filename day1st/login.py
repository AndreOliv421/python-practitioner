print("SISTEMA ADMINISTRATIVO")

usuario = input("Digite o usuári: ")
senha = input("Digite a senha: ")

if usuario == "admin":
    if senha == "123456":
        print("Login bem sucedido!")
    else:
        print("Senha incorreta")
else:
    print("Usuário inválido")
