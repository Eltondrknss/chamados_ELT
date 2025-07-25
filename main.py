from manager import GestorDeChamados

def mostrar_menu():
    print("\n--- Menu Principal do Sistema de Chamados ---")
    print("1. Abrir um novo chamado")
    print("2. Visualizar todos os chamados")
    print("3. Buscar um chamado por ID")
    print("4. Atualizar Status de um Chamado")
    print("5. Deletar um chamado")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main():
    gestor = GestorDeChamados()

    while True:
        escolha = mostrar_menu()

        if escolha == '1':
            print("\n---- Abrir novo chamado ----")
            titulo = input("Titulo do chamado: ")
            descricao = input("Descrição detalhada do problema: ")
            solicitante = input("Seu nome: ")

            gestor.criar_novo_chamado(titulo, descricao, solicitante)

        elif escolha == '2':
            print("\n---- Lista de Chamados ----")
            chamados = gestor.consultar_todos_chamados()
            if not chamados:
                print("Nenhum chamado encontrado.")
            else:
                print(f"{'ID':<5}{'Titulo':<30}{'Solicitante':<20}{'Status':<15}{'Data de Criação'}")
                print("-" * 90)

                for chamado in chamados:
                    id_chamado, titulo, solicitante, status, data_criacao = chamado
                    data_formatada = data_criacao.strftime("%d/%m/%y %H:%M")
                    print(f"{id_chamado:<5}{titulo:<30}{solicitante:<20}{status:<15}{data_formatada}")

        elif escolha == '3':
            print("\n---- Buscar Chamado por ID ----")
            try:
                id_chamado = int(input("Digite o ID do chamado: "))
                chamado = gestor.encontrar_chamado_por_id(id_chamado)
                if not chamado:
                    print(f"Chamado com o ID {id_chamado} não encontrado.")
                else:
                    id_c, titulo, desc, sol, data_c, status = chamado
                    print("\n--- Detalhes do Chamado ---")
                    print(f"ID: {id_c}, Status: {status}")
                    print(f"Aberto em: {data_c.strftime('%d/%m/%Y às %H:%M:%S')}")
                    print(f"Solicitante: {sol}, Título: {titulo}")
                    print("----------------------------")
                    print(f"Descrição:\n{desc}")
                    print("----------------------------")
                    # if status:
                    #     print(f"Status:\n{status}")
            except ValueError:
                print(id_chamado)
                print("Erro! Por favor, digite um ID válido")

        elif escolha == '4':
            print("\n---- Atualizar Status de um Chamado ----")
            try:
                id_chamado = int(input("Digite o ID do chamado que deseja atualizar: "))
                novo_status = input("Digite o novo sutatus (Em Andamento, Resolvido): ")
                gestor.atualizar_status_do_chamado(id_chamado, novo_status)
            except ValueError:
                print("Erro: Por favor digite um ID válido.")

        elif escolha == '5':
            print("\n---- Deletar um Chamado ----")
            try:
                id_chamado = int(input("Digite o ID do chamado para deletar: "))
                confirmacao = input(f"Tem certeza que deseja deletar o chamado {id_chamado}? (s/n)")
                if confirmacao.lower() == 's':
                    gestor.deletar_chamado_por_id(id_chamado)
                    print(f"Chamado ID {id_chamado} excluído!")
                else:
                    print("Operação cancelada.")
            except ValueError:
                print("Erro: Por favor digite um ID válido.")

        elif escolha == '6':
            print("Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida. Por favor escolha uma das listadas.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()