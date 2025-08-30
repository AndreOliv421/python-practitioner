
# Sistema de Tarefas
tarefas = [] # lista vazia

while True:
    print("=== MENU TAREFAS ===")
    print("1 - Adicionar Tarefa")
    print("2 - Listar tarefas")
    print("9 - Sair do Sistema")

    opcao = input("Esolha sua opção")

    # Adicionar Tarefa
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
    
    # append -> Adicionar a Lista
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    # Listar Tarefas
    elif opcao == "2":
        # len -> length -> tamanho
        if len(tarefas) == 0:
            print("Não existem tarefas cadastadas")
        else:
            for tarefa in tarefas:
                print(tarefa)
    elif opcao == "9":
        print("Saindo do Sistema")
        break
    else:
        print("Opção inexistente, tente novamente...")