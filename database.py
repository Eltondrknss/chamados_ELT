import pymssql

DB_SERVER = 'DESKTOP-VRE32VN'
DB_USER = 'eltondrk'
DB_PASSWORD = 'eltonabc'
DB_NAME = 'ChamadosELT'

def conectar(): # funçao pra conectar no banco com retorno de erro em caso de falha
    try:
        conn = pymssql.connect(
            server = DB_SERVER,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME
        )
        return conn
    except pymssql.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
    
def criar_chamado(titulo, descricao, solicitante):
    # insere um novo chamado na tabela Chamados
    conn = None
    try:
        conn = conectar()
        if conn:
            # cursor = objeto que executa os comandos sql
            cursor = conn.cursor()

            # comando sql usando placeholders
            sql = "INSERT INTO Chamados (Titulo, Descricao, Solicitante) VALUES (%s, %s, %s)"

            # executa a query passando os dados de forma segura
            cursor.execute(sql, (titulo, descricao, solicitante))

            # confirma a transacao e salva no banco
            conn.commit()

            print("Chamado aberto com sucesso!!!")
            return True
        
    except pymssql.Error as e:
        if conn:
            conn.rollback*() #desfaz a transacao caso der erro
        return False
    
    finally:
        # fecha a conexao dando certo ou nao
        if conn:
            conn.close()

def listar_todos_chamados():
    # busca os chamados da tabela e retorna uma lista de tuplas
    conn = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            sql = "SELECT ID, Titulo, Solicitante, Status, DataCriacao FROM Chamados ORDER BY ID DESC"
            cursor.execute(sql)

        chamados = cursor.fetchall() # fetchall() busca todos os resultados da consulta
        return chamados
    
    except pymssql.Error as e:
        print(f"Erro ao listar chamados: {e}")
        return [] # retornar lista vazia em caso de erro
    
    finally:
        if conn:
            conn.close()

def buscar_chamado_por_ID(id_chamado):
    # busca um chamado pelo ID. Retorna uma tupla com os dados do chamado ou None se nao encontrar
    conn = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM Chamados WHERE ID = %s"
            cursor.execute(sql, (id_chamado))
            chamado = cursor.fetchone() #fetchone() busca apenas o primeiro resultado da consulta
            return chamado
        
    except pymssql.Error as e:
        print(f"Erro ao buscar chamado: {e}")
        return None
    finally:
        if conn:
            conn.close()

def atualizar_status_chamado(id_chamado, novo_status):
    conn = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()

            sql = "UPDATE Chamados SET Status = %s WHERE ID = %s"
            cursor.execute(sql, (novo_status, id_chamado))

            conn.commit()

            # rowcount diz quantas linhas foram afetadas
            # se for maior que zero, funcionou
            if cursor.rowcount > 0:
                return True
            else:
                return False
            
    except pymssql.Error as e:
        print("Erro ao atualizar o chamado: {e}")
        if conn:
            conn.rollback() # desfaz a alteraçao se der erro
        return False
    
    finally:
        if conn:
            conn.close()

def deletar_chamado(id_chamado):
    conn = None
    try:
        conn = conectar()
        if conn:
            cursor = conn.cursor()

            sql = "DELETE FROM Chamados WHERE ID = %s"
            cursor.execute(sql, (id_chamado))

            conn.commit()

            if cursor.rowcount > 0:
                return True
            else:
                return False
            
    except pymssql.Error as e:
        print(f"Eror ao deletar o chamado: {e}")
        if conn:
            conn.rollback()
        return False
    
    finally:
        if conn:
            conn.close()