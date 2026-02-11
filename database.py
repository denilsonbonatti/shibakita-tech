import pyodbc
from tkinter import messagebox

#Configurações do Servidor e Banco de dados

SERVIDOR = "xxx"
BANCO = "ShibakitaEletro"

#Credenciais de usuário

USUARIO_APP = "azure-senac"
SENHA_APP = "xxx"

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
        #messagebox.showinfo("Sucesso", "Conectado ao banco de dados com êxito!")
        return conexao
        
    except Exception as e:
        # Se houver erro, ele cai aqui
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar:\n{e}")
        return None
    
def realizar_login(login_digitado, senha_digitada):
    """Verifica na tabela de Usuarios se as credenciais batem."""
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        # Buscamos o perfil para saber se o usuário existe
        comando = "SELECT Perfil FROM Usuarios WHERE Login = ? AND Senha = ?"
        cursor.execute(comando, (login_digitado, senha_digitada))
        
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            return resultado[0] # Retorna 'Administrador' ou 'Operador'
    return None

