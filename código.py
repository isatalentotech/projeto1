import json

def criar_tarefa(tarefas):
    nova_tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"tarefa": nova_tarefa, "concluida": False})
    salvar_tarefas(tarefas)

def listar_tarefas(tarefas):
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i+1}. {tarefa['tarefa']} ({status})")

def marcar_como_concluida(tarefas):
    indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
    tarefas[indice]["concluida"] = True
    salvar_tarefas(tarefas)

def editar_tarefa(tarefas):
    indice = int(input("Digite o número da tarefa a ser editada: ")) - 1
    nova_tarefa = input("Digite a nova descrição: ")
    tarefas[indice]["tarefa"] = nova_tarefa
    salvar_tarefas(tarefas)

def excluir_tarefa(tarefas):
    indice = int(input("Digite o número da tarefa a ser excluída: ")) - 1
    del tarefas[indice]
    salvar_tarefas(tarefas)

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Criar nova tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Editar tarefa")
        print("5. Excluir tarefa")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            criar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_como_concluida(tarefas)
        elif opcao == "4":
            editar_tarefa(tarefas)
        elif opcao == "5":
            excluir_tarefa(tarefas)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
