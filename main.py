from database import criar_chamado, listar_todos_chamados, buscar_chamado_por_ID, atualizar_status_chamado
import datetime

def novo_chamado_interface():
    print("\n---- Abrir novo chamado ----")
    titulo = input("Titulo do chamado: ")
    descricao = input("Descrição detalhada do problema: ")
    solicitante = input("Seu nome: ")

    if not titulo or not descricao:
        # validaçao de campos em branco
        print("\nErro: Titulo e Descrição são campos obrigatórios.")
        return
    
    # cria o chamado
    criar_chamado(titulo, descricao, solicitante)

def visualizar_chamados_interface():
    print("\n---- Lista de Chamados ----")
    chamados = listar_todos_chamados()

    if not chamados:
        print("Nenhum chamado encontrado.")
        return
    
    print(f"{'ID':<5}{'Titulo':<30}{'Solicitante':<20}{'Status':<15}{'Data de Criação'}")
    print("-" * 90)

    for chamado in chamados:
        id_chamado, titulo, solicitante, status, data_criacao = chamado
        data_formatada = data_criacao.strftime("%d/%m/%y %H:%M")
        print(f"{id_chamado:<5}{titulo:<30}{solicitante:<20}{status:<15}{data_formatada}")

def buscar_chamado_interface():
    print("\n---- Buscar Chamado por ID ----")
    try:
        id_input = input("Digite o ID do chamado: ")
        id_chamado = int(id_input)
    except ValueError:
        print("Erro! Por favor, digite um ID válido.")
        return
    
    chamado = buscar_chamado_por_ID(id_chamado)

    if not chamado:
        print(f"Chamado com o ID {id_chamado} não encontrado.")
        return
    
     # desempacota todos os dados do chamado
    id_c, titulo, desc, sol, data_c, status = chamado
    
    print("\n--- Detalhes do Chamado ---")
    print(f"ID: {id_c}")
    print(f"Status: {status}")
    print(f"Aberto em: {data_c.strftime('%d/%m/%Y às %H:%M:%S')}")
    print(f"Solicitante: {sol}")
    print(f"Título: {titulo}")
    print("----------------------------")
    print(f"Descrição:\n{desc}")
    print("----------------------------")

def atualizar_chamado_interface():
    print("\n---- Atualizar Status de um Chamado ----")
    try:
        id_input = input("Digite o ID do chamado que deseja atualizar: ")
        id_chamado = int(id_input)
    except ValueError:
        print("Erro: Por favor digite um ID válido")
        return
    
    # BOA PRATICA: verificar se o chamado existe antes de alterar
    chamado = buscar_chamado_por_ID(id_chamado)
    if not chamado:
        print(f"Erro: Chamado com ID: {id_chamado} não encontrado.")

    print(f"Status atual do chamado {id_chamado}: {chamado[-1]}") # o status é o ultimo item da tupla

    novo_status = input("Digite o novo status (Ex: Em Andamento, Fechado): ")

    if not novo_status:
        print("Erro: O novo status não pode ser vazio.")
        return
    
    sucesso = atualizar_status_chamado(id_chamado, novo_status)
    if sucesso:
        print("Status do chamado atualizado com sucesso")
    else:
        print("Não foi possivel atualizar o status do chamado.")

def main():
    while True:
        print("\n--- Menu Principal do Sistema de Chamados ---")
        print("1. Abrir um novo chamado")
        print("2. Visualizar todos os chamados")
        print("3. Buscar um chamado por ID")
        print("4. Atualizar Status de um Chamado")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            novo_chamado_interface()
        elif escolha == '2':
            visualizar_chamados_interface()
        elif escolha == '3':
            buscar_chamado_interface()
        elif escolha == '4':
            atualizar_chamado_interface()
        elif escolha == '5':
            print("Obrigado por usar o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ =="__main__":
    main()














# def main():
#     print("----- Bem-vindo ao sistema de chamados -----")

#     novo_chamado_interface()

#     print("\nPrograma encerrado.")

# # garante que a funçao main() só vai rodar se for direto do arquivo main.py
# if __name__ == "__main__":
#     main()


























# from database import conectar


# def main():
#     print("-----Sistema de chamados-----")
#     conn = conectar()

#     if conn:
#         print("Banco conectado com sucesso!!!")

#         #adicionar logica do menu

#         conn.close()
#         print("Desconectado da base de dados.")
#     else:
#         print("Falha ao conectar ao banco de dados. Encerrando o programa.")

# if __name__ == "__main__":
#     main()
