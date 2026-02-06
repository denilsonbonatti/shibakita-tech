import pyodbc
from tkinter import messagebox

# Configurações do Servidor e Banco
SERVIDOR = 'xxx'
BANCO = 'ShibakitaEletro'

# Credenciais do Usuário (definidas no portal Azure)
USUARIO_APP = 'xxxx' 
SENHA_APP = 'xxxx'

def conectar():
    string_conexao = (
        f"Driver={{ODBC Driver 17 for SQL Server}};" 
        f"Server=tcp:{SERVIDOR},1433;"               
        f"Database={BANCO};"
        f"UID={USUARIO_APP};"
        f"PWD={SENHA_APP};"
        "Encrypt=yes;"                               
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    
    try:
        # Tenta estabelecer a conexão
        conexao = pyodbc.connect(string_conexao)
        
        # Se chegou aqui, deu certo!
        messagebox.showinfo("Sucesso", "Conectado ao banco de dados com êxito!")
        return conexao
        
    except Exception as e:
        # Se houver erro, ele cai aqui
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar:\n{e}")
        return None