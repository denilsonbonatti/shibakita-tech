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
    
    # Título Principal
    lbl_titulo = ctk.CTkLabel(janela_clie, text="GESTÃO DE CLIENTES", font=("Roboto", 24, "bold"))
    lbl_titulo.pack(pady=20)

    # Frame do Formulário
    frame_form = ctk.CTkFrame(janela_clie, corner_radius=10)
    frame_form.pack(padx=30, pady=10, fill="both", expand=True)

    # Campo ID (Desabilitado - Gerado pelo Banco)
    ctk.CTkLabel(frame_form, text="ID Cliente (Auto):", font=("Roboto", 12)).pack(anchor="w", padx=20, pady=(15, 0))
    ent_id = ctk.CTkEntry(frame_form, placeholder_text="ID", state="disabled", fg_color="#2b2b2b")
    ent_id.pack(fill="x", padx=20, pady=5)

    # Campo Nome
    ctk.CTkLabel(frame_form, text="Nome Completo:", font=("Roboto", 12)).pack(anchor="w", padx=20, pady=(10, 0))
    ent_nome = ctk.CTkEntry(frame_form, placeholder_text="Digite o nome do cliente...")
    ent_nome.pack(fill="x", padx=20, pady=5)

    # Campo CPF
    ctk.CTkLabel(frame_form, text="CPF:", font=("Roboto", 12)).pack(anchor="w", padx=20, pady=(10, 0))
    ent_cpf = ctk.CTkEntry(frame_form, placeholder_text="000.000.000-00")
    ent_cpf.pack(fill="x", padx=20, pady=5)

    # Campo Telefone
    ctk.CTkLabel(frame_form, text="Telefone:", font=("Roboto", 12)).pack(anchor="w", padx=20, pady=(10, 0))
    ent_tel = ctk.CTkEntry(frame_form, placeholder_text="(00) 00000-0000")
    ent_tel.pack(fill="x", padx=20, pady=5)

    # Campo Endereço
    ctk.CTkLabel(frame_form, text="Endereço:", font=("Roboto", 12)).pack(anchor="w", padx=20, pady=(10, 0))
    ent_end = ctk.CTkEntry(frame_form, placeholder_text="Rua, Número, Bairro, Cidade")
    ent_end.pack(fill="x", padx=20, pady=5)


    janela_clie.mainloop()