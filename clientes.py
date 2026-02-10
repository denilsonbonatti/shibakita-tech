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

    # --- FUNÇÕES DE INTERFACE (Ações dos Botões) ---
    def acao_limpar():
        ent_id.configure(state="normal")
        ent_id.delete(0, "end")
        ent_id.configure(state="disabled")
        ent_nome.delete(0, "end")
        ent_cpf.delete(0, "end")
        ent_tel.delete(0, "end")
        ent_end.delete(0, "end")

    # --- LAYOUT ---
    
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

    # --- CONTAINER DE BOTÕES (CRUD) ---
    frame_botoes = ctk.CTkFrame(janela_clie, fg_color="transparent")
    frame_botoes.pack(fill="x", padx=30, pady=20)

    # Botão Salvar (Create)
    btn_salvar = ctk.CTkButton(frame_botoes, text="SALVAR", fg_color="#22c55e", hover_color="#16a34a", 
                               font=("Roboto", 14, "bold"), width=120)
    btn_salvar.grid(row=0, column=0, padx=5, pady=5)

    # Botão Atualizar (Update)
    btn_atualizar = ctk.CTkButton(frame_botoes, text="ATUALIZAR", fg_color="#3b82f6", hover_color="#2563eb", 
                                  font=("Roboto", 14, "bold"), width=120)
    btn_atualizar.grid(row=0, column=1, padx=5, pady=5)

    # Botão Excluir (Delete)
    btn_excluir = ctk.CTkButton(frame_botoes, text="EXCLUIR", fg_color="#ef4444", hover_color="#dc2626", 
                                font=("Roboto", 14, "bold"), width=120)
    btn_excluir.grid(row=0, column=2, padx=5, pady=5)

    # Botão Limpar
    btn_limpar = ctk.CTkButton(frame_botoes, text="LIMPAR", fg_color="#64748b", hover_color="#475569", 
                               font=("Roboto", 14, "bold"), width=120, command=acao_limpar)
    btn_limpar.grid(row=0, column=3, padx=5, pady=5)

    # Configuração das colunas do grid para ficarem iguais
    frame_botoes.grid_columnconfigure((0,1,2,3), weight=1)

    # Label de Status (Opcional para feedback visual)
    lbl_status = ctk.CTkLabel(janela_clie, text="Pronto para cadastro.", text_color="gray")
    lbl_status.pack(side="bottom", pady=10)

    janela_clie.mainloop()