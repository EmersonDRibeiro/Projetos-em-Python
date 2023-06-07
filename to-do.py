def exibir_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas na lista.")
    else:
        for nome, descricao in tarefas.items():
            print(f"Tarefa: {nome}")
            print(f"Descrição: {descricao}")
            print("------------------------")

def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefas[nome] = descricao
    print("Tarefa adicionada com sucesso.")

def remover_tarefa(tarefas):
    nome = input("Digite o nome da tarefa que deseja remover: ")
    if nome in tarefas:
        del tarefas[nome]
        print("Tarefa removida com sucesso.")
    else:
        print("Tarefa não encontrada.")

def main():
    tarefas = {}
    while True:
        print("----- Aplicativo de Lista de Tarefas -----")
        print("1. Exibir Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo do aplicativo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
