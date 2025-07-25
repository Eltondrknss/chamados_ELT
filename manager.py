import database

class GestorDeChamados:

    def criar_novo_chamado(self, titulo, descricao, solicitante):
        if not titulo or not descricao or not solicitante:
            print(">>>> ERRO: Todos os campos são obrigatórios")
            return False
        
        sucesso = database.criar_chamado(titulo, descricao, solicitante)
        if sucesso:
            print(">>>> Chamado aberto com sucesso!")
            return sucesso
    
    def consultar_todos_chamados(self):
        return database.listar_todos_chamados()
    
    def encontrar_chamado_por_id(self, id_chamado):
        return database.buscar_chamado_por_ID(id_chamado)
    
    def atualizar_status_do_chamado(self, id_chamado, novo_status):
        chamado_existente = self.encontrar_chamado_por_id(id_chamado)
        if not chamado_existente:
            print(f">>>> ERRO: Chamado com o ID {id_chamado} não encontrado")
            return False
        
        if not novo_status:
            print(">>>> ERRO: O novo status não pode ser vazio")
            return False
        
        sucesso = database.atualizar_status_chamado(id_chamado, novo_status)
        if sucesso:
            print(f"Status do chamado {id_chamado} atualizado com sucesso!")
            return sucesso
        
    def deletar_chamado_por_id(self, id_chamado):
        chamado_existente  = self.encontrar_chamado_por_id(id_chamado)
        if not chamado_existente:
            print(f">>>> ERRO: Chamado com o ID {id_chamado} não encontrado.")
            return False
        
        sucesso = database.deletar_chamado(id_chamado)
        return sucesso