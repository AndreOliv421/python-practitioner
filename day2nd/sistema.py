
    # Sistema gerenciador de Nomes
#nomes = []

#def menu():
     # print("=== Menu ===")
     
    # print("1 - Adicionar Nome")
    # print("2 - Listar Nomes")
   #  print("3 - Remover nome")
  #   print("9 - Sair do Sistema")
 #    return input("Escolha sua opção: ")
    
#while  True:
   # opcao = menu() 

# Gerenciador de Nomes Simples

nomes = []  # lista para armazenar os nomes

def menu():
    print("\n===== GERENCIADOR DE NOMES =====")
    print("1 - Adicionar nome")
    print("2 - Listar nomes")
    print("3 - Remover nome")
    print("4 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        nome = input("Digite o nome que deseja adicionar: ")
        nomes.append(nome)
        print(f"✅ Nome '{nome}' adicionado com sucesso!")

    elif opcao == "2":
        if nomes:
            print("\n📋 Lista de nomes:")
            for i, n in enumerate(nomes, start=1):
                print(f"{i}. {n}")
        else:
            print("⚠ Nenhum nome cadastrado.")

    elif opcao == "3":
        if nomes:
            nome = input("Digite o nome que deseja remover: ")
            if nome in nomes:
                nomes.remove(nome)
                print(f"🗑 Nome '{nome}' removido com sucesso!")
            else:
                print(f"❌ Nome '{nome}' não encontrado.")
        else:
            print("⚠ Nenhum nome para remover.")

    elif opcao == "4":
        print("👋 Saindo do gerenciador. Até logo!")
        break

    else:
        print("❌ Opção inválida, tente novamente.")