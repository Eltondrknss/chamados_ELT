from database import criar_chamado

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

def main():
    print("----- Bem-vindo ao sistema de chamados -----")

    novo_chamado_interface()

    print("\nPrograma encerrado.")

# garante que a funçao main() só vai rodar se for direto do arquivo main.py
if __name__ == "__main__":
    main()


























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
