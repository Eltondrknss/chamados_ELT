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
            