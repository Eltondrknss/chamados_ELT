# Sistema de Gerenciamento de Chamados 

Um sistema de help desk simples para gerenciar chamados de suporte técnico, desenvolvido em Python com armazenamento em SQL Server.

##  Funcionalidades

-  Criar novos chamados
-  Listar todos os chamados
-  Buscar chamados por ID 
-  Atualizar status de chamados
-  Deletar chamados

##  Requisitos

- Python 3.x
- SQL Server
- Bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

##  Configuração

1. Clone este repositório
2. Crie um arquivo `.env` com as seguintes variáveis:

```env
DB_SERVER=seu_servidor
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=ChamadosELT
```

##  Estrutura do Banco de Dados

O sistema utiliza uma tabela `Chamados` com:

| Campo | Tipo |
|------|------|
| ID | int (auto-increment) |
| Titulo | varchar |
| Descricao | text |
| Solicitante | varchar |
| Status | varchar |
| DataCriacao | datetime |

##  Como Usar

Execute o sistema com:

```bash
python main.py
```

### Menu de Opções:

1. Abrir um novo chamado
2. Visualizar todos os chamados
3. Buscar um chamado por ID
4. Atualizar Status de um Chamado
5. Deletar um chamado
6. Sair

##  Estrutura do Projeto

- `main.py` - Interface principal do sistema
- `manager.py` - Gerenciamento de regras de negócio
- `database.py` - Operações do banco de dados