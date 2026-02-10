import customtkinter as ctk
from tkinter import messagebox

def abrir_janela_clientes():
    """Cria a interface para o CRUD de Clientes."""
    
    # Configuração da Janela (Sub-janela do Menu)
    janela_clie = ctk.CTkToplevel()
    janela_clie.title("Shibakita Tech - Gestão de Clientes")
    janela_clie.geometry("600x700")
    janela_clie.resizable(False, False)
    
    # Garante que esta janela fique no topo e impeça interação com o menu atrás
    janela_clie.grab_set()

    janela_clie.mainloop()